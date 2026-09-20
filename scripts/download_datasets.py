import os
import subprocess
import sys

DATASETS = [
    {
        "name": "WSN-DS",
        "kaggle_ref": "bassamkasasbeh1/wsnds",
        "target_dir": "datasets/wsn-ds",
        "description": "Wireless Sensor Network Dataset (WSN-DS.csv)"
    },
    {
        "name": "AWID (AWID-CLS-R-Trn.csv)",
        "kaggle_ref": "zhiqingcui/awidclsr",
        "target_dir": "datasets/awid",
        "description": "Aegean Wi-Fi Intrusion Dataset reduced classification set"
    },
    {
        "name": "AWID3",
        "kaggle_ref": "anikatab/awid3-5csv",
        "target_dir": "datasets/awid3",
        "description": "Aegean Wi-Fi Intrusion Dataset 3"
    },
    {
        "name": "CIC-IoT-2023",
        "kaggle_ref": "himadri07/ciciot2023",
        "target_dir": "datasets/cic-iot-2023",
        "description": "UNB Canadian Institute for Cybersecurity IoT 2023 dataset"
    },
    {
        "name": "Edge-IIoTset",
        "kaggle_ref": "mohamedamineferrag/edgeiiotset-cyber-security-dataset-of-iot-iiot",
        "target_dir": "datasets/edge-iiotset",
        "description": "Edge Industrial IoT cybersecurity dataset"
    },
]

def download_all():
    print("=" * 60)
    print("  Cybersecurity & IoT Datasets Automator")
    print("=" * 60)
    
    for ds in DATASETS:
        print(f"\n[+] Downloading: {ds['name']}")
        print(f"    Description: {ds['description']}")
        print(f"    Destination: {ds['target_dir']}")
        
        os.makedirs(ds['target_dir'], exist_ok=True)
        cmd = [
            "kaggle", "datasets", "download",
            "-d", ds['kaggle_ref'],
            "-p", ds['target_dir'],
            "--unzip"
        ]
        
        try:
            result = subprocess.run(cmd, check=True)
            print(f"    [OK] Downloaded and extracted successfully.")
        except subprocess.CalledProcessError as err:
            print(f"    [ERROR] Failed to download {ds['name']}: {err}")
        except FileNotFoundError:
            print("    [ERROR] Kaggle CLI is not installed or not in PATH.")
            print("            Install via: pip install kaggle")
            sys.exit(1)

if __name__ == "__main__":
    download_all()
