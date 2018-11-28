
def handle_output(naomi, ken, N, caseno):
    succ = N
    naomi1 = list(naomi)
    ken1 = list(ken)
    for i in range(0,N):
        if (naomi[0] < ken[-1] and naomi[0]<ken[0]):
            succ -= 1
        if (naomi[0] > ken[0]):
            del(ken[0])
        else:
            del(ken[-1])
        del(naomi[0])
    #print(succ1)

    succ1 = N
    for i in range(0,N):
        if naomi1[-1] < ken1[-1]:
            succ1 -= 1
            del(ken1[-1])
        else:
            del(ken1[0])
        del(naomi1[-1])
    #print(succ1)

    with open('output.txt', 'a') as fo:
        outstr = 'Case #'+ str(caseno) + ': '+str(succ)+' '+str(succ1)+'\n'
        fo.write(outstr)

    

with open('output.txt', 'w')as fo:
    pass

with open('input.txt') as fi:
    T = int(fi.readline())
    for t in range(1, T+1):
        N = int(fi.readline())
        naomi = [float(x) for x in fi.readline().split(' ')]
        ken = [float(x) for x in fi.readline().split(' ')]
        #print(sorted(naomi), sorted(ken))
        handle_output(sorted(naomi), sorted(ken), N, t)
