from random import randint
import connection

#   Register User
def register_user(user):
    id = randint(100,999)
    fname = user[0]
    lname = user[1]
    email = user[2]
    passwd = user[3]

    chk = check_email_id(id, email)

    if (chk == 1):
        print("Oops..!! ID Or Email Id already Exist")
    else:
        print("Hii "+fname+"..!! We Are Creating Your Account")
        token = randint(10000,99999)

        # print(id,fname, lname, email, passwd, token)
        finaluser = (id, fname, lname, email, passwd, token)

        insert_query = "insert into user (id, fname, lname, email, pass, token, evs)  values(%s, %s, %s, %s, %s, %s, 'Inactive')"

        con = connection.getconnection();
        mycursor = con.cursor();
        mycursor.execute(insert_query, finaluser)
        con.commit()

# Check user exist or not by email or id
def check_email_id(uid, email):
    check_query = "select id, email from user where id=%s or email=%s"
    con = connection.getconnection();
    user = (uid, email)
    data = con.cursor()
    data.execute(check_query, user)
    for dt in data:
        if(dt[0] == uid, dt[1] == email):
            return 1
        else:
            return 0
    con.commit()

# User Profile
def user_profile(id):
    get_profile = "select *from user where id=%s"
    con = connection.getconnection()

    id = (id, )
    user_details = con.cursor()
    user_details.execute(get_profile,id)
    row = user_details.fetchone()

    if user_details.rowcount == -1:
        print("No Profile Found on this ID")
    else:
        print("------------------- Profile Details -----------------")
        for u in row:
            print(u,end=" ")
    con.commit()

# Update Profile
def update_user(up_details):

    update_query = "update user set fname=%s, lname=%s, pass=%s where id=%s"
    con = connection.getconnection()
    updated_user = con.cursor()
    updated_user.execute(update_query, up_details)
    con.commit()

# Delete User
def delete_user(id):

    chk = check_email_id(id, " ")
    if chk == 1:
        del_user_query = "delete from user where id = %s"
        con = connection.getconnection()
        mycursor = con.cursor()
        mycursor.execute(del_user_query, (id,))
        if mycursor.rowcount  > -1:
            print("Profile Deleted Successfully")
        else:
            print("Something Went Wrong")
        con.commit()
    else:
        print("ID Not Exist..Enter Correct ID")