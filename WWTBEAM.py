# WHO WANTS TO BE A MILLIONAIRE #

class Main:
    def __init__(self, userName):
        self.userName = userName

    def __repr__(self):
        return self.userName

    def greetings(self):
        print("Welcome To The Game " + self.userName + "!")


name = input("Enter User Name:")

User1 = Main(name)
User1.greetings()