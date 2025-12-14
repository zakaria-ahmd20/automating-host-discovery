# Nmap Host Discovery → IP Extractor

A lightweight Python automation script that performs **Nmap host discovery**, extracts **valid IPv4 addresses** from normal Nmap output (`-oN`), **filters out network addresses (`.0`)**, and prepares a clean target list for **port scanning**.

This project is designed for **fast internal network reconnaissance** and practical security workflows.

---

## ✨ Features

* Runs **Nmap ping scan** automatically
* Parses **plain-text Nmap output** (`targets.txt`)
* Extracts **valid IPv4 addresses only**
* Filters out **network addresses ending in `.0`**
* Outputs a clean list to `ips.txt`
* Ready for direct use with `nmap -iL`

---

## 🛠 Requirements

* Python 3.x
* Nmap (installed and accessible in PATH)
* Linux / Kali Linux recommended

---

## 📂 Files

```
.
├── scan.py        # Main automation script
├── targets.txt   # Raw Nmap output (auto-generated)
├── ips.txt       # Clean IP list for port scanning
└── README.md
```

---

## 🚀 Usage

### 1️⃣ Run the script

```bash
python3 scan.py
```

This will:

* Run an Nmap ping scan on `192.168.18.0/24`
* Save results to `targets.txt`
* Extract valid host IPs into `ips.txt`

---

### 2️⃣ Port scan extracted hosts

```bash
nmap -iL ips.txt -p- -sS -T4
```

---

## 🧠 How It Works (Quick)

1. Nmap discovers live hosts using ARP/TCP/UDP probes
2. Python reads the **text output** line by line
3. Regex extracts valid IPv4 addresses
4. A second regex filters out `.0` network addresses
5. Remaining IPs are written to `ips.txt`

---

## 🔍 Regex Used

### IPv4 validation

```regex
\b(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}\b
```

### Network address exclusion (`.0`)

```regex
\b(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\.(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\.(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\.0\b
```

---

## ⚠️ Notes

* Intended for **authorized internal network testing only**
* `.0` addresses are excluded to avoid scanning network IDs
* Script can be easily extended to exclude `.255` or deduplicate IPs

---

## 📌 Why This Exists

This project focuses on **speed, simplicity, and practical recon**, using:

* Regex-based parsing (fast and flexible)
* Plain-text Nmap output (human + machine friendly)
* Minimal dependencies

Ideal for:

* Network engineers
* Security students
* CTF / lab environments
* Internal asset discovery

---

## 🧑‍💻 Author

Built for learning and practical network security automation.

---

## 📜 License

Use responsibly. Educational and internal testing purposes only.
