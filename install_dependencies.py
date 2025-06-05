import subprocess
import sys
import os

def install_dependencies():
    """Install required dependencies for the portfolio website."""
    print("Installing dependencies...")
    
    # Check if requirements.txt exists
    if not os.path.exists('requirements.txt'):
        print("Creating requirements.txt file...")
        with open('requirements.txt', 'w') as f:
            f.write("Flask==2.3.3\n")
            f.write("Flask-WTF==1.2.1\n")
            f.write("WTForms==3.1.1\n")
            f.write("email-validator==2.1.0\n")
            f.write("Werkzeug==2.3.7\n")
    
    try:
        # Uninstall any existing conflicting packages first
        print("Uninstalling any existing packages...")
        subprocess.run([sys.executable, '-m', 'pip', 'uninstall', '-y', 'Flask', 'Flask-WTF', 'WTForms', 'email-validator', 'Werkzeug'], 
                      capture_output=True)
        
        # Install dependencies using pip
        print("Installing new packages...")
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
        print("Dependencies installed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error installing dependencies: {e}")
        print("Please try manually: pip install -r requirements.txt")

if __name__ == "__main__":
    install_dependencies()
