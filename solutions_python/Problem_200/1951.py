from sys import stdin as cin

cases=int(cin.readline())

''' A brute-force method that does not work quickly enough

def is_tidy(n):
    num=str(n)
    for i in range(len(num)-1):
        if int(num[i])>int(num[i+1]):
            return False
    return True


for case in range(1, cases+1):
    n=int(cin.readline())
    while not is_tidy(n):
        n-=1
    print("Case #"+str(case)+":", n)
'''

for case in range(1, cases+1):
    n=cin.readline().strip()
    for i in range(len(n)-1, 0, -1):
        #print(i, end=' ')
        index=i
        change_prior=True
        while index<len(n) and int(n[index])<int(n[index-1]):
            #print('Changing', n[:i], end=' ')
            if change_prior:
                n=str(int(n[0:index])-1)+'9'+n[index+1:]
                change_prior=False
            else:
                n=n[0:index]+'9'+n[index+1:]
            index+=1
            #print(n, end=' ')
        #print()
    if len(n)>1:
        n=n.strip('0')
    print("Case #"+str(case)+":", n)
        