class user:
    username = ""
    userpass = ""
javad = user
javad.username = "T22"
javad.userpass = "123456"
def identify (username1,password1):
# inja etelaat ro tatabogh mide
    if username1 == "user":
        if password1 == javad.userpass:
            print("Logged in")
    else:
        print("incorrect")
