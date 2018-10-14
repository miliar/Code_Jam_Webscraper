x = int(input())
for i in range(x):
    shy,secu = input().split()
    total = 0
    num = 0
    for x in range(int(shy)+1):
        if secu[x] != '0':
            if total + num >= x:
                pass
            else:
                num += x - (total+num)
##                print(x,total,num)
            total += int(secu[x])
        else:
            pass
        
    print('Case #'+str(i+1)+':',num)
