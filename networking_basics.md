1. ifconfig
Old utility to view and configure network interfaces; mostly replaced now.
Shows IP, MAC, and interface status but lacks newer features.

2. ip addr
Displays IP addresses assigned to interfaces.
Part of the modern iproute2 suite—replaces ifconfig.

3. ip link
Shows and configures the state of network interfaces (UP/DOWN, MAC).
Useful for enabling/disabling interfaces or changing MTU/MAC.

4. ip route
Displays the kernel routing table—shows where packets go.
Helps trace default gateway and subnet-specific routing.
