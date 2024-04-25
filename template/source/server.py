import os

try:
    portf = open("./port.txt", "r")
except:
    print("Error: Could not load up './port.txt'")
    exit()

port = portf.read()
os.system(f"python -m http.server {port}")