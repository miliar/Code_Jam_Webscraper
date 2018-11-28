def flip(cake, N):
    if N < len(cake):
        if cake[N]=='+':
            cake[N]='-'
        elif cake[N]== '-':
            cake[N]='+'
intN=input()
cake=[]
maximums = []
cnt = 0
for i in range(intN):
    inputS=raw_input().split()
    S = inputS[0]
    for i in S:
        cake.append(i)
    num = int(inputS[1])
    for i in range(len(cake)-num+1):
        if cake[i]=='-':
           for j in range(num):
                flip(cake,(i+j))
           cnt+=1
    if cake.__contains__('-'):
        maximums.append(-1)
    else:
        maximums.append(cnt)
    cnt = 0
    cake=[]
for i in range(len(maximums)):
    if maximums[i]==-1:
        print 'Case #%d: IMPOSSIBLE' %(i+1)
    else:
        print 'Case #%d: %d' %(i+1,maximums[i])





