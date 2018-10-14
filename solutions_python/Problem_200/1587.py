T = input()
for test in range(1,T+1):
    def chk(num):
        li = list(str(num))
        if (li==sorted(li)):
            return 1
        else:
            return 0
    N = input()
    for x in range(N,0,-1):
        if chk(x)==1:
            print ('Case #'+str(test)+': '+str(x))
            break
