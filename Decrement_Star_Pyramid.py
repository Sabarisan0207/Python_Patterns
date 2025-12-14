n=int(input())
sum=n* (n+1)//2
for i in range(n,0,-1):
    for j in range(i):
        print(sum,end='')
        sum -= 1
        if j!=i-1 :
            print("*",end='')
    print()
