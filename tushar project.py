def prime(a):
    if a<=1:
        return("Composite")
    elif a==2:
        return("Prime")
    else:
        for i in range(2,a):
            if a%i==0:
                return("Composite")
        else:
            return("Prime")
n=int(input("Enter a number: "))
c=0
pp=1
if n<1:
    print("Enter valid number")
else:
    while True:
        if prime(pp)=="Prime":
            if str(pp)==str(pp)[::-1]:
                c+=1
                if c==n:
                    break
                else:
                    pp+=1
            else:
                pp+=1
        else:
            pp+=1
    print(n,"th Prime Palindrome number is: ",pp,sep="")
