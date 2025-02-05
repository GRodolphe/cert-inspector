from cryptography import x509
from cryptography.hazmat.backends import default_backend
from datetime import datetime
import os
import sys
from pathlib import Path

def format_certificate_info(certificate):
    """Format certificate information in a clean way"""
    info = []
    info.append("=" * 50)
    
    # Subject CN (if exists)
    subject_cn = next((attr.value for attr in certificate.subject if attr.oid._name == 'commonName'), None)
    if subject_cn:
        info.append(f"Certificate for: {subject_cn}")
    
    info.append("-" * 50)
    
    # Basic Information
    info.append("SUBJECT:")
    for attribute in certificate.subject:
        info.append(f"  {attribute.oid._name}: {attribute.value}")

    info.append("\nISSUER:")
    for attribute in certificate.issuer:
        info.append(f"  {attribute.oid._name}: {attribute.value}")

    info.append("\nVALIDITY:")
    info.append(f"  From: {certificate.not_valid_before.strftime('%Y-%m-%d %H:%M:%S')}")
    info.append(f"  Until: {certificate.not_valid_after.strftime('%Y-%m-%d %H:%M:%S')}")

    # Status
    now = datetime.utcnow()
    if now < certificate.not_valid_before:
        status = "NOT YET VALID"
    elif now > certificate.not_valid_after:
        status = "EXPIRED"
    else:
        status = "VALID"
    info.append(f"\nSTATUS: {status}")

    info.append("=" * 50 + "\n")
    return "\n".join(info)

def analyze_certificate_file(cert_path):
    """Analyze a single certificate file"""
    try:
        with open(cert_path, 'rb') as cert_file:
            cert_data = cert_file.read()
            certificate = x509.load_pem_x509_certificate(cert_data, default_backend())
            return format_certificate_info(certificate)
    except Exception as e:
        return f"Error processing {cert_path}: {str(e)}\n"

def find_certificates(path):
    """Find all potential certificate files in directory"""
    cert_extensions = {'.pem', '.crt', '.cer', '.der'}
    if os.path.isfile(path):
        return [path]
    
    cert_files = []
    for root, _, files in os.walk(path):
        for file in files:
            if any(file.lower().endswith(ext) for ext in cert_extensions):
                cert_files.append(os.path.join(root, file))
    return cert_files

def main():
    if len(sys.argv) != 2:
        print("Usage: python cert_analyzer.py <path_to_certificate_or_directory>")
        sys.exit(1)

    path = sys.argv[1]
    
    if not os.path.exists(path):
        print(f"Error: Path '{path}' does not exist")
        sys.exit(1)

    cert_files = find_certificates(path)
    
    if not cert_files:
        print("No certificate files found!")
        sys.exit(1)

    print(f"\nFound {len(cert_files)} certificate file(s)\n")
    
    for cert_file in cert_files:
        print(f"File: {cert_file}")
        result = analyze_certificate_file(cert_file)
        print(result)

if __name__ == "__main__":
    main()
