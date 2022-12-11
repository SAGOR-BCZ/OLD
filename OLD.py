import os, sys
try:
    __import__("old_enc").Main()
except Exception as e:
    exit(str(e))
