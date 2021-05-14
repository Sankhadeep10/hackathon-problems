n=int(input("Enter the number of shocks"))
ar=[]
for i in range(n):
    x=int(input())
    ar.append(x)
y=set(ar)
s=0
for e in y:
    s+=(ar.count(e))//2
print(s)

