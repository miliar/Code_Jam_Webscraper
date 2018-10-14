a=int(input())
b=a
f = open('out_flip.txt', 'w')
while a>0:
    a-=1
    s, k = input().split()
    s, k = [str(s), int(k)]
    sl=list(s)
    l = len(sl)
    cnt = 0
    for i in range(0,l-k+1):
        if sl[i]!='+':
            cnt += 1
            for j in range(i,i+k):
                if sl[j]!='+':
                    sl[j]='+'
                else:
                    sl[j]='-'
    s="".join(sl)
    if s==l*'+':
        print('Case #' + str(b - a) + ': ' + str(cnt))
        f.write('Case #' + str(b - a) + ': ' + str(cnt) + '\n')
    else:
        print('Case #' + str(b - a) + ': ' + 'IMPOSSIBLE')
        f.write('Case #' + str(b - a) + ': ' + 'IMPOSSIBLE'+'\n')
f.close()
