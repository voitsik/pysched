import requests
from importlib.metadata import (
    PackageNotFoundError,
    version as distribution_version,
)
from packaging import version

try:
    pysched_version = distribution_version("pythonSCHED")
except PackageNotFoundError:
    pysched_version = "unknown"

def get_latest_version():
    response = requests.get("https://pypi.org/pypi/pythonSCHED/json")
    response.raise_for_status()
    return response.json()["info"]["version"]

def check_version():
    try:
        latest_version = get_latest_version()
        if version.parse(pysched_version) < version.parse(latest_version):
            print(f"Version {latest_version} of pySCHED is available through "
                  f"pip,\n you are running version {pysched_version}.")
    except Exception:
        pass
