n=int(input("enter the number"))
a=open("w3-4.txt","r")
c=[]
for line in (a.readlines() [-n:]):
    print(line,end="")
    c.append(line)
print(c)
a.close()