
def trip(st_from, st_to, how_many, N):
    #print "st_from, st_to, how_many, N:", st_from, st_to, how_many, N
    if st_from == st_to:
        return 0
    diff = st_to - st_from
    #print "diff:", diff
    if diff < 0:
        #print "ERROR!!!"
        return 1000000000
    #print "val: ", how_many*(2*N - diff-1)*(diff)/2
    return how_many*(2*N - (diff-1))*(diff)/2
    """ind = 0
    res =0
    for _ in xrange(st_from, st_to):
        res += (N-ind)
        ind += 1
    return res*how_many"""
    
import sys

T = int(sys.stdin.readline())
for case in xrange(1, T+1):
    [N, M] = map(int, sys.stdin.readline().split())
    l = []
    d = {}
    l_uczciwe = []
    for _ in xrange(M):
        [o, e, p] = map(int, sys.stdin.readline().split())
        l_uczciwe.append([o, e, p])
        d[o] = d.get(o, 0)+p
        d[e] = d.get(e, 0)-p
    l = []
    for key, v in d.iteritems():
        if v!= 0:
            l.append([key, v])
    
    l = sorted(l, key=lambda x: x[0])#;l ma pola na ktorej stacji, ilu
    #print "l:", l
    
    result = 0
    kkk = 0
    while len(l) > 0:
        kkk+=1
        #chcemy pierwszego elementu sie pozbyc:
        accumulated = [l[0][1]] # accumulated ma pole ilu, indeks odpowiada l
        if accumulated[0] == 0:
            l = l[1:]
            continue
        
        minimas = [(l[0][1], 0)] #ma pola: ilu, indeks z accumulated/listy l
        for ind in xrange(1, len(l)):
            val = l[ind][1]
            new_val = accumulated[-1] + val
            accumulated.append(new_val)
            if new_val < minimas[-1][0]:
               minimas.append((new_val, ind))
            if new_val == 0:
                break
        #print "accumulated:", accumulated
        #print "minimas:", minimas
        #break
        this_far = 0#how many guys went out, from the back
        for last_ind in reversed(range(1, len(minimas))):
            
            #print "wysiadaja na stacji: ", l[minimas[last_ind][1]][0], " wysiada ich: ", minimas[last_ind-1][0] - this_far
            result += trip(l[0][0], l[minimas[last_ind][1]][0], minimas[last_ind-1][0] - this_far, N )#od, do, ilu
            #print "zmieniamy:", l[minimas[last_ind][1]]
            l[minimas[last_ind][1]][1] += minimas[last_ind-1][0] - this_far
            this_far += minimas[last_ind-1][0] - this_far
            if this_far == l[0][1]:
                break
        
        l = l[1:]
        
    
    #print "result:", result
    
    result_uczciwe = 0
    for o, e, p in l_uczciwe:
        result_uczciwe += trip(o, e, p, N)
    #print "result_uczciwe:", result_uczciwe    
    print "Case #"+str(case)+": "+str((result_uczciwe - result) % 1000002013)
