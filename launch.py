import subprocess
import os
import time
import webbrowser

def run_npm(open: bool=False):
    print(os.getcwd())
    print(os.path.abspath("agenthub"))
    os.chdir("/teamspace/studios/this_studio/OS/AIOS/agenthub")
    if "node_modules" not in os.listdir():
        install_process = subprocess.Popen(["npm", "install"])
        install_process.wait()
    subprocess.Popen(["npm", "run", "dev"])
    if open:
        time.sleep(5)
        webbrowser.open_new_tab("http://localhost:3000")

if __name__ == "__main__":
    run_npm(True)
