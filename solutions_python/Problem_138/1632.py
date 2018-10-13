t = int(raw_input())
for test in range(1,t+1):
    num = int(raw_input())
    n = map(float,raw_input().split(' '))
    k = map(float,raw_input().split(' '))
    Naomi = list(n)
    Ken = list(k)
    Naomi.sort()
    Ken.sort()
    found = 0
    while len(Naomi)!=0:
        if(Naomi[0] < Ken[0]):
                del Naomi[0]
                del Ken[len(Ken)-1]
        else:
                del Naomi[0]
                del Ken[0]
                found += 1
    score = 0
    n.sort()
    k.sort()
    while num:
        if n[num-1]>k[num-1]:
            n.pop()
            del k[0]
            num -= 1
            score += 1
        else:
            n.pop()
            k.pop()
            num -= 1
    print 'Case #{}: {} {}'.format(test,found,score)
