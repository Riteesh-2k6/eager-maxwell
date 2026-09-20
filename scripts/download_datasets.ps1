<#
.SYNOPSIS
    Automated downloader for WSN-DS, AWID, AWID3, CIC-IoT-2023, and Edge-IIoTset datasets using Kaggle CLI.
#>

$ErrorActionPreference = "Stop"

$datasets = @(
    @{ Name = "WSN-DS"; Ref = "bassamkasasbeh1/wsnds"; Target = "datasets/wsn-ds" },
    @{ Name = "AWID"; Ref = "zhiqingcui/awidclsr"; Target = "datasets/awid" },
    @{ Name = "AWID3"; Ref = "anikatab/awid3-5csv"; Target = "datasets/awid3" },
    @{ Name = "CIC-IoT-2023"; Ref = "himadri07/ciciot2023"; Target = "datasets/cic-iot-2023" },
    @{ Name = "Edge-IIoTset"; Ref = "mohamedamineferrag/edgeiiotset-cyber-security-dataset-of-iot-iiot"; Target = "datasets/edge-iiotset" }
)

Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host "  Cybersecurity & IoT Datasets Downloader (PowerShell)" -ForegroundColor Cyan
Write-Host "==========================================================" -ForegroundColor Cyan

foreach ($ds in $datasets) {
    Write-Host "`n[+] Downloading $($ds.Name)..." -ForegroundColor Green
    Write-Host "    Target Directory: $($ds.Target)" -ForegroundColor Gray
    
    New-Item -ItemType Directory -Force -Path $ds.Target | Out-Null
    kaggle datasets download -d $ds.Ref -p $ds.Target --unzip
    
    Write-Host "    [OK] Finished downloading $($ds.Name)" -ForegroundColor Yellow
}

Write-Host "`n[✔] All datasets downloaded and extracted successfully!" -ForegroundColor Green
