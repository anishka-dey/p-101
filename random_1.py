import random
response="y"
while response=="y":
    no=random.randint(1,6)
    if no==1:
        print("[-----]\n[     ]\n[  0  ]\n[     ]\n[-----]")
    elif no==2:
        print("[-----]\n[     ]\n[0   0]\n[     ]\n[-----]")
    elif no==3:
        print("[-----]\n[     ]\n[0 0 0]\n[     ]\n[-----]")
    elif no==4:
        print("[-----]\n[0   0]\n[     ]\n[0   0]\n[-----]")
    elif no==5:
        print("[-----]\n[0   0]\n[  0  ]\n[0   0]\n[-----]")
    elif no==6:
        print("[-----]\n[0 0 0]\n[     ]\n[0 0 0]\n[-----]")
    response=input("Type y to continue or n to stop")