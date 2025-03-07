# 🔍 SQL-XSS-LFI Vulnerability Scanner

## 🚀 Description
The **SQL-XSS-LFI Vulnerability Scanner** is an automated security tool designed to identify potential vulnerabilities in web applications. It leverages advanced **Google Dorking** techniques to discover URLs that may be susceptible to:

- 🛡️ **SQL Injection (SQLi)**
- 🔥 **Cross-Site Scripting (XSS)**
- 📂 **Local File Inclusion (LFI)**

This tool utilizes **Google, Bing, and Yandex** search engines to find potential targets and systematically test them for security flaws.

---

## ✨ Features
✅ **Automated Dork Scanning** – Searches for vulnerable URLs using search engines.  
✅ **SQL Injection Detection** – Identifies possible SQLi vulnerabilities.  
✅ **XSS Testing** – Checks for cross-site scripting flaws.  
✅ **LFI Exploitation Detection** – Scans for local file inclusion vulnerabilities.  
✅ **TOR Integration** – Uses the TOR network to anonymize requests.  
✅ **Multi-Threaded Execution** – Speeds up scanning by testing multiple URLs simultaneously.  

---

## 📥 Installation

### 🔹 Prerequisites
Ensure you have **Python 3.x** installed on your system. Additionally, you need the **TOR service** running before executing the script.

### 🔹 Install Dependencies
Run the following command to install the required Python libraries:

```bash
pip install requests pysocks google
```

### 🔹 Start the TOR Service
Before running the script, ensure the TOR service is active:

```bash
sudo service tor start  # Linux
```

🔹 **Windows Users:** Open the **TOR browser** and keep it running.

---

## ⚡ Usage

To run the scanner, execute:

```bash
python dork_scanner.py
```

You'll be prompted to enter a **Google Dork query**. The script will then retrieve URLs and test them for vulnerabilities.

### 📌 Example:
```
Enter Google Dork: inurl:index.php?id=
Found 35 relevant URLs. Testing for vulnerabilities...
[VULNERABLE] http://example.com/index.php?id=1
    - SQL Injection (Payload: ' OR 1=1 --)
[SAFE] http://secure-site.com/index.php?id=5
```

---

## ⚠️ Disclaimer
> **This tool is intended for educational and security research purposes only.**  
> **Unauthorized scanning of systems you do not own is illegal and unethical.**  
> **The author is not responsible for any misuse of this tool.**  

---

👨‍💻 **Developed with ❤️ by [Your Name]**  
📜 Licensed under MIT  
