def FlipTheCake(data,flip):
    l=[]
    count  = 0
    for  i in range(len(data)):
        l.append(data[i])
    for  j in range(len(l)):
        if j+flip <=len(l):
            if l[j] == '-':
                count = count +1
                for k in range(j, j + flip):
                    if l[k] == '-':
                        l[k] = '+'
                    else:
                        l[k] = '-'
        else:
            if '-' in l:
                return 'IMPOSSIBLE'
            else:
                return count

tc = int(input())
for  i in range (1,tc+1):
    inp , flip= input().split(' ')
    flip = int(flip)
    #for  i in range(len(inp)):
    if '-' in inp:
        res = FlipTheCake(inp , flip)
        print("Case #%d: "%i+str(res))

    else:
        print('Case #%d: '%i,0)