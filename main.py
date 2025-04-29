# main.py
from subnet import calculate_subnet

def main() -> None:
    print("Simple Subnet Calculator\n")
    ip_input = input("Enter IP Address (e.g., 192.168.1.1): ").strip()
    cidr_input = input("Enter Subnet Mask (CIDR, e.g., 24): ").strip()

    try:
        results = calculate_subnet(ip_input, cidr_input)
        print("\nResults:")
        for key, value in results.items():
            print(f"{key.replace('_', ' ').title()}: {value}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
