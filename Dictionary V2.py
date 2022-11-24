print("-----------------------------")
print("MENU:")
print("1 -> Add an item")
print("2 -> Search")
print("3 -> Exit (y/n)")
print("-----------------------------")

dict_info =  {"Mark": ["19", "Manila", "09123456789"]}

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
        userInfo = dict_info[fullName] = {"age": age,
                             "address": address,
                             "country": country,
                             "phone number": phoneNumber,
                             "gender": gender,
                             "email": email,
                             }
        userList = dict_info.update(userInfo)
        print("Saved!")