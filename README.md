# Secure File Storage System

Flask web app for secure file upload, encryption, and decryption using AES + RSA (Hybrid Encryption).

## 1. Create Virtual Environment

### Windows

python -m venv venv

venv\Scripts\activate

### Mac / Linux

python3 -m venv venv

source venv/bin/activate

## 2. Install Dependencies

pip install flask flask_sqlalchemy werkzeug pycryptodome

### 3. Run the Project

python app.py

Open:

http://127.0.0.1:5000/

### 4. Required Folders

Make sure these folders exist:

uploads/

encrypted/

crypto/

templates/

### 5. Notes

SQLite database will be created automatically

RSA keys are generated during user registration

Original uploaded files are deleted after encryption