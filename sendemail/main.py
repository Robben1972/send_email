from signedup import signedupdef
from signin import signindef

take = 0
while True:
    print("1. Sign in")
    print("2. Sign up")
    print("3. Exit")
    try:
        section = int(input("Choose: "))
        take = section
    except ValueError:
        print("Choose again")
    if 3 >= take >= 1:
        if take == 1:
            signindef()
        elif take == 2:
            signedupdef()
        elif take == 3:
            break
    else:
        print("Choose again")




