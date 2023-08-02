from datetime import date
now = date.today()

take1 = int(input("Enter 1 to add the item and Enter 2 to retrieve value : "))
if take1 == 1:
    take2 = int(input("Enter 1 for diet plan and 2 for exercise sheet :"))
    if take2 == 1:
        name = input("Enter your name : ")
        f = open(f"{name} diet plan.txt","a")
        w1 = input(" write : ")
        f.write(str(now.strftime("%d/%m/%y (%H:%M:%S) ")) + "--> " + w1 + "\n")
        f.close
    elif take2 == 2:
        name = input("Enter your name : ")
        f = open(f"{name} Exercise sheet.txt", "a")
        w1 = input(" write : ")
        f.write(str(now.strftime("%d/%m/%y (%H:%M:%S) ")) + "--> " + w1 + "\n")
        f.close
elif take1 == 2:
    take3 = int(input(" Enter 1 to see your diet plan and 2 to see exercise sheet : "))
    if take3 == 1:
        fname = input("Enter the name : ")
        s = open(f"{fname} diet plan.txt","r")
        content = s.read()
        print(content)
        s.close()
    elif take3 == 2:
        fname = input("Enter the name : ")
        s = open(f"{fname} Exerxise sheet.txt", "r")
        content = s.read()
        print(content)
        s.close()
