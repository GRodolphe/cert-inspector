# Certificate Inspector

A Python utility for analyzing X.509 certificates. This tool can inspect individual certificate files or recursively scan directories for certificates, providing detailed information about each certificate found.

## Features
- Analyze single certificate files or entire directories
- Support for multiple certificate formats (.pem, .crt, .cer, .der)
- Display key certificate information:
  - Subject Common Name
  - Full subject details
  - Issuer information
  - Validity period
  - Current validity status

## Requirements
- Python 3.6+
- cryptography library

Install the required dependency using pip:
```bash
pip install cryptography
```

## Usage
```bash
python cert-inspector.py <path_to_certificate_or_directory>
```

### Examples
Analyze a single certificate:
```bash
python cert-inspector.py /path/to/certificate.pem
```
Scan a directory for certificates:
```bash
python cert-inspector.py /path/to/certificates/directory
```

## Output Format
For each certificate, the tool displays:
- File path
- Certificate subject (Common Name)
- Complete subject information
- Issuer details
- Validity period
- Current status (VALID, EXPIRED, or NOT YET VALID)

## Supported Certificate Extensions
- .pem - Privacy Enhanced Mail certificates
- .crt - Certificate files
- .cer - Certificate files
- .der - DER encoded certificates

## Error Handling
The tool provides error messages for:
- Invalid file paths
- Malformed certificates
- Directories with no certificate files
- Incorrect usage
