x=float(input('Enter the first number'))
y=float(input('Enter the second number'))
sum=x+y
if x%2==0 and y%2==0:
    print (sum)
elif x%2!=0 and y%2!=0:
    if x>y:
        difference=x-y
    else:
        difference=y-x
        print(difference)
else:
    print(x ,y)

