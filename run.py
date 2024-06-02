import os
import sys
import subprocess
from dotenv import load_dotenv  # pip: python-dotenv

print('Starting WhisperWriter...')
load_dotenv()
script_dir = os.path.dirname(os.path.realpath(__file__))
subprocess.run([sys.executable, os.path.join(script_dir, 'src', 'main.py')])
