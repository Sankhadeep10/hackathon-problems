n=int(input("Enter the number upto which you want to check"))
for i in range(1,n+1):
    if(i%2!=0 and i%3!=0):
        print(i)