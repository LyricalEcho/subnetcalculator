# subnet.py
import ipaddress

def calculate_subnet(ip_input: str, cidr_input: str) -> dict:
    """
    Calculate and return subnet information.
    """
    cidr = int(cidr_input)
    if not (0 <= cidr <= 32):
        raise ValueError("CIDR must be between 0 and 32.")
    
    ip_with_cidr = f"{ip_input}/{cidr}"
    network = ipaddress.ip_network(ip_with_cidr, strict=False)
    first_usable = list(network.hosts())[0] if network.num_addresses > 2 else network.network_address
    last_usable = list(network.hosts())[-1] if network.num_addresses > 2 else network.broadcast_address

    return {
        "network_address": str(network.network_address),
        "broadcast_address": str(network.broadcast_address),
        "first_usable": str(first_usable),
        "last_usable": str(last_usable),
        "usable_hosts": network.num_addresses - 2 if network.num_addresses > 2 else 0
    }
