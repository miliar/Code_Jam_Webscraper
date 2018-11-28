# cook your dish here
def tidy(n):
    for i in range(len(n)-1):
        if n[i]>n[i+1]:
            return False
    return True
t=int(input())
for ji in range(t):
    n=input()
    print("Case #",ji+1,": ",sep='',end='')
    if tidy(n):
       print(n)
    else:
        while not tidy(n):
            p=int(n)-1
            n=str(p)
        print(n)    
        