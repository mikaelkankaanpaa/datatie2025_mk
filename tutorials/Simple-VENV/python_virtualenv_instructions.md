# Creating a Python Virtual Environment (Windows & macOS)

## ✅ Windows

1. Open **Command Prompt**.
2. Navigate to your project directory:
   ```bash
   cd path\to\your\project
   ```
3. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
4. Activate the virtual environment:
   ```bash
   venv\Scripts\activate
   ```

---

## ✅ macOS

1. Open **Terminal**.
2. Navigate to your project directory:
   ```bash
   cd /path/to/your/project
   ```
3. Create a virtual environment:
   ```bash
   python3 -m venv venv
   ```
4. Activate the virtual environment:
   ```bash
   source venv/bin/activate
   ```

Now, you are ready to install JupyterLab and other libraries:
   ```bash
   pip install jupyterlab
   ```