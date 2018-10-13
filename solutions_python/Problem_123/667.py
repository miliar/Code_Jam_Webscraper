from math import log,ceil

def coups(longMotes,motes,init):
    if init == 1:
        return longMotes
    if longMotes == 0:
        return 0
    if init > motes[0]:
        return coups(longMotes-1,motes[1:],init+motes[0])
    puiss2 = ceil(log(float(motes[0])/(init-1),2))
    if puiss2 >= longMotes:
        return longMotes
    else:
        return int(puiss2) + coups(longMotes,motes,2**puiss2 * (init-1) + 1)

def traitement(titre):
    f_in = open(titre+'.in','r')
    T = int(f_in.readline())
    f_out = open(titre+'.out','w')
    for k in range(1,T+1):
        init,longmotes = tuple(map(int,f_in.readline().split()))
        motes = list(map(int,f_in.readline().split()))
        motes.sort()
        f_out.write('Case #{}: {}\n'.format(k,coups(longmotes,motes,init)))
    f_out.close()
    f_in.close()

traitement('A-small-attempt4')
