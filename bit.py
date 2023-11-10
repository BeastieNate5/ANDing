class Bi:
    def __init__(self):
        # Stores the octets of the given IP
        self.octs = {
            1 : None,
            2 : None,
            3 : None,
            4 : None
        }

        # Stores the octets of the subnet mask
        self.subOcts = {
            1 : None,
            2 : None,
            3 : None,
            4 : None
        }

        # Stores the octets of the anded IP
        self.andedIP = {
            1 : None,
            2 : None,
            3 : None,
            4 : None
        }

    # This method gets the given IP from the user
    def get_ip(self):
        userInput = input("Enter IP address: ")

        splitInput = userInput.split(".")
        x=1
        
        # Makes sure the list is four which means it has 4 octets
        if len(splitInput) == 4:
            for oct in splitInput:

                # This will try to parse the octet to a int
                try:
                    int(oct)
                # If it fails to parse the octet then return the function
                except:
                    print("Invalid numbers, try again")
                    return self.get_ip()
                
                # Makes sure they dont put invalid IP address binary values
                if int(oct) > 255 or int(oct) < 0:
                    print("One of the octs were higher than 255")
                    return self.get_ip()
                
                # If it passes all the filttering then add the octet to self.octets
                self.octs[x] = int(oct)
                x += 1

        else:
            print("Enter correct bi format")
            return self.get_ip()
    
    # Almost the extact same as the get_ip() method
    def get_subnet(self):
        userInput = input("Enter subnet mask: ")

        splitInput = userInput.split(".")
        x=1
        if len(splitInput) == 4:
            for oct in splitInput:
                try:
                    int(oct)
                except:
                    print("Invalid numbers, try again")
                    return self.get_subnet()

                if int(oct) > 255 or int(oct) < 0:
                    print("One of the octs were higher than 255")
                    return self.get_subnet()
                 
                self.subOcts[x] = int(oct)
                x += 1

        else:
            print("Enter correct bi format")
            return self.get_subnet()
    
    # Displays IP in a clean format
    def display_IP(self):
        return f"{self.octs[1]}.{self.octs[2]}.{self.octs[3]}.{self.octs[4]}"
    
    # Displays subnet mask in a clean format
    def display_subnet(self):
        return f"{self.subOcts[1]}.{self.subOcts[2]}.{self.subOcts[3]}.{self.subOcts[4]}"
    
    # Displays anded IP in a clean format
    def display_andedIP(self):
        return f"{self.andedIP[1]}.{self.andedIP[2]}.{self.andedIP[3]}.{self.andedIP[4]}"

    # This method does the anding
    def anding(self):
        for x in range(1,5):
            self.andedIP[x] = self.octs[x] & self.subOcts[x]


bi = Bi()
bi.get_ip()
bi.get_subnet()
bi.anding()

print("")
print("======================================================")
print(f"Given IP: {bi.display_IP()}")
print(f"Subnet Mask: {bi.display_subnet()}")
print(f"Anded: {bi.display_andedIP()}")
print("======================================================")