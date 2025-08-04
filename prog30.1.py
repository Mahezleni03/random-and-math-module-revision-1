valid = False
while not valid:
    try:
        age = int(input("Enter your age: "))
        while age % 2 == 0:
            print("!!BYE!!")
        valid = True
    except ValueError:
        print("ERROR: Please enter numbers only")