x = int(input())

def carryOver(s,i):
    if i >= 0 and int(s[i]) > int(s[i+1]):
        s[i] = str(int(s[i])-1)
        for j in range(i+1,len(s)):
            s[j] = str(9)
        carryOver(s,i-1)

for j in range(x):
    s = list(input())
    for i in range(len(s) - 1):
        carryOver(s,i)

    print("Case #{}: ".format(j+1), end = '')
        
    for i in s:
        if i != '0':
            print(i,end='')

    print('')
