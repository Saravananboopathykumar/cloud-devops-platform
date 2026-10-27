import shutil

usage = shutil.disk_usage("/")

print("Disk Total:", usage.total)
print("Disk Free:", usage.free)
