n=int(input("Enter the no of elements you want in  the series :  "))
u=0
v=1
for i in range(0,n):
    print(u)
    u=v
    v=u+v
