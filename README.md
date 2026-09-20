# Cybersecurity & IoT Intrusion Detection Datasets

This repository provides automated scripts and documentation to find, download, and structure 5 major cybersecurity and IoT/IIoT intrusion detection datasets:

1. **WSN-DS** (`WSN-DS.csv`) - Wireless Sensor Network DoS Attack Dataset
2. **AWID** (`AWID-CLS-R-Trn.csv`) - Aegean Wi-Fi Intrusion Dataset (Reduced 14-feature classification set)
3. **AWID3** - Aegean Wi-Fi Intrusion Dataset 3 (802.11ac Enterprise Wi-Fi Attacks)
4. **CIC-IoT-2023** - Canadian Institute for Cybersecurity IoT Dataset 2023
5. **Edge-IIoTset** - Comprehensive Edge & Industrial IoT Cybersecurity Dataset

---

## 🚀 Quick Start: Downloading Datasets

### Prerequisites
1. Install Python 3 & Kaggle CLI:
   ```bash
   pip install kaggle
   ```
2. Configure your Kaggle API key (`kaggle.json` placed in `~/.kaggle/`).

### Option A: Python Script
Run the automated Python downloader script:
```bash
python scripts/download_datasets.py
```

### Option B: PowerShell Script (Windows)
Run the PowerShell downloader script:
```powershell
.\scripts\download_datasets.ps1
```

---

## 📁 Directory Structure
When downloaded, files will be saved in the following local directory structure:
```
eager-maxwell/
├── scripts/
│   ├── download_datasets.py
│   └── download_datasets.ps1
└── datasets/
    ├── wsn-ds/          # WSN-DS.csv
    ├── awid/            # AWID-CLS-R-Trn.csv
    ├── awid3/           # AWID3 CSV feature files
    ├── cic-iot-2023/    # CICIoT2023 train/test/val splits
    └── edge-iiotset/    # Edge-IIoTset Attack & Normal traffic
```
