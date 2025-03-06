# SQL-XSS-LFI Vulnerability Scanner

## Description
The **SQL-XSS-LFI Vulnerability Scanner** is an automated security tool designed to identify potential vulnerabilities in web applications. It leverages advanced dorking techniques to discover URLs that may be susceptible to:

- **SQL Injection (SQLi)**
- **Cross-Site Scripting (XSS)**
- **Local File Inclusion (LFI)**

This tool uses Google, Bing, and Yandex search engines to find potential targets and then systematically tests them for security flaws.

---

## Features
- **Automated Dork Scanning**: Searches for vulnerable URLs using search engines.
- **SQL Injection Detection**: Identifies possible SQLi vulnerabilities.
- **XSS Testing**: Checks for cross-site scripting flaws.
- **LFI Exploitation Detection**: Scans for local file inclusion vulnerabilities.
- **TOR Integration**: Uses the TOR network to anonymize requests.
- **Multi-Threaded Execution**: Speeds up scanning by testing multiple URLs simultaneously.

---

## Installation
### Prerequisites
Ensure you have **Python 3.x** installed on your system. Additionally, you need the TOR service to be running before executing the script.

### Required Libraries
Install the necessary Python libraries by running the following command:

```bash
pip install requests PySocks googlesearch-python
```

### Starting TOR Service
Before running the scanner, ensure that the TOR service is active:

**Linux/macOS:**
```bash
sudo service tor start
```
**Windows (Command Prompt):**
```cmd
tor.exe
```

---

## Usage
Run the script and enter a Google Dork query to identify potential vulnerabilities:

```bash
python dork_scanner.py
```

You will be prompted to enter a Google Dork query (e.g., `inurl:index.php?id=`), after which the tool will retrieve URLs and test them for vulnerabilities.

---

## Disclaimer
🚨 **This tool is intended strictly for ethical hacking and educational purposes.** Unauthorized scanning or penetration testing of websites without explicit permission is illegal and punishable by law. The developer is not responsible for any misuse of this tool.

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.

