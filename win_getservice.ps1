#!powershell
# WANT_JSON
# POWERSHELL_COMMON

$data = Get-Service | Format-Table -Property Status, Name;

$result = New-Object psobject @{
    changed = $false
    Services = $data
};