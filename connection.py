import mysql.connector

def getconnection():
    con = mysql.connector.connect(host="localhost", user="root", passwd="", database="resumebuilder")
    if con:
        # print("Success")
        return con
    else:
        print("Failed to Connect")