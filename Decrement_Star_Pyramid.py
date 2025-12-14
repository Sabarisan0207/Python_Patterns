n=int(input())
sum=n* (n+1)//2
for i in range(n,0,-1):
    for j in range(i):
        print(sum,end='')
        sum -= 1
        if j!=i-1 :
            print("*",end='')
    print()

    #2
n=int(input())
for row in range(n):
    for j in range (row):
        print(row+1,end='')
    print()
