print("-----------------------------")
print("MENU:")
print("1 -> Add an item")
print("2 -> Search")
print("3 -> Exit (y/n)")
print("-----------------------------")

dict_store =  {"Mark": ["19", "Manila", "09123456789"]}

while True:

    choice = int(input("What do you want to do? (1-3) "))

    if choice == 1:
        fullName = input("Name: ")
        age = int(input("Age: "))
        address = input("Address: ")
        country = input("Country: ")
        phoneNumber = input("Phone Number: ")
        gender = input("Gender: ")
        email = input("Email: ")
        
        dataOfUser = {
            "Full Name": fullName,
            "Age": age,
            "Address": address,
            "Country": country,
            "Phone Number": phoneNumber,
            "Gender": gender,
            "email": email,
        }

        print("Saved!")

        dict_store[fullName] = userInfo

    elif choice == 2:
        fullName_other = input("Enter your full name: ")
        if fullName_other in dict_store:
            searchForData = dict_store[fullName_other]
            for key, value in searchForData.items():
                print(key, ":", value)
    
    elif choice == 3:
        exit = input("Are you sure? (Yes/No) ")
        if exit == "Yes":
            break