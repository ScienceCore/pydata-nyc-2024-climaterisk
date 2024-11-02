# This script generates .netrc file, prompting user for EarthData credentials.
# Delete or rename ~/.netrc before executing this script (it won't overwrite a
# pre-existing ~/.netrc file).

from getpass import getpass
from pathlib import Path
import sys

NETRC_PATH = Path('~/.netrc').expanduser()
TEMPLATE = " ".join(["machine", "urs.earthdata.nasa.gov", "login",
                     "{USERNAME}", "password", "{PASSWORD}\n"])

if NETRC_PATH.exists():
    print(f"\nWarning: {NETRC_PATH} exists already (this script won't overwrite).\n")
    print(f"         Back up {NETRC_PATH} first & delete to avoid losing credentials.")
    sys.exit(1)

username = input("\nNASA EarthData login:    ")
password = getpass(prompt="\nNASA EarthData password: ")

print(f"\nWriting EarthData credentials supplied to {NETRC_PATH}")
NETRC_PATH.write_text(TEMPLATE.format(USERNAME=username, PASSWORD=password))
print(f"Modifying permissions on {NETRC_PATH}\n")
NETRC_PATH.chmod(0o600)
