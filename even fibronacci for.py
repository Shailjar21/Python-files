n1=0
n2=1
count=1
print(n1)
for i in range(6):
    n=n1+n2
    n1=n2
    n2=n
    if n%2==0:
        print(n)
        count=count+1
print('Task is completed and even number of terms',count)
