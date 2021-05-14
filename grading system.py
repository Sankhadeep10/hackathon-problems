n=int(input())
ar=[]
for i in range(n):
    x=int(input())
    ar.append(x)
for i in range(n):
    if(ar[i]>=38 and (ar[i]%5)>=3):
        ar[i]+=5-(ar[i]%5)
    print(ar[i],end=" ")
        