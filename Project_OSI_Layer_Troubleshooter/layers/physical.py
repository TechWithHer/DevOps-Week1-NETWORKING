import os
#Check network interface status.
def check_physical():
    os.system("ip link show")
