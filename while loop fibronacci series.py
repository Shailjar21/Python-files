n1=int(input('Enter the first number'))
n2=int(input('Enter the second number'))
terms=int(input('enter the no. of terms'))
count=0
while count<terms:
    print(n1)
    n=n1+n2
    n1=n2
    n2=n
    count=count+1
print('Task is completed')
