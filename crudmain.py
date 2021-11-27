import crud_operation as co
print("Welcome to Crud Application")

while "true" :
    print("1 - Register User\t2 - Display User\t3 - Update User\t4 - Delete User")
    ch = (int)(input("Enter Choice : "))
    if ch == 1:
        fname = input("Enter First Name : ")
        lname = input("Enter Last Name : ")
        email = input("Enter Email : ")
        passwd = input("Enter Password : ")
        User = (fname, lname, email, passwd)
        co.register_user(User)

    elif ch == 2:
        id = (int)(input("Enter ID To Display Profile Details : "))
        co.user_profile(id)

    elif ch == 3:
        print("* You Can't Update ID and Email")
        id = (int)(input("Enter ID to update Profile : "))
        co.user_profile(id)
        fname = input("\nEnter First Name ")
        lname = input("Enter Last Name ")
        passwd = input("Enter Password : ")
        updated_details = (fname, lname, passwd, id)
        co.update_user(updated_details)

    elif ch == 4:
        id = (int)(input("Enter ID to Delete Profile : "))
        co.delete_user(id)
    ch = (int(input("\nIf You Want To Continue Press 1 : ")))
    if ch != 1:
        break
print("------ thank you-------")