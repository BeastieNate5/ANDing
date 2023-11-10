import anding


if __name__ == "__main__":
    ip_addr = anding.IP()
    ip_addr.get_ip()
    ip_addr.get_subnet()
    ip_addr.anding()

    print("")
    print("======================================================")
    print(f"Given IP: {ip_addr.display_IP()}")
    print(f"Subnet Mask: {ip_addr.display_subnet()}")
    print(f"Anded: {ip_addr.display_andedIP()}")
    print("======================================================")