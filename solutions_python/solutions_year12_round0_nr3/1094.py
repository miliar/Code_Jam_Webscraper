import itertools 

def isRecycled(n, m):
    n = str(n)
    m = str(m)
    for i in range(len(n)):
        if n[i] == m[0]:
            n_circ = itertools.cycle(n)
            for k in range(i):
                d_n = n_circ.next()
            m_circ = itertools.cycle(m)
            for j in range(len(m)):
                d_n = n_circ.next()
                d_m = m_circ.next()
                if d_n != d_m:
                    break
                elif j == len(m)-1:
                    return True        
    return False


num_cases = int(raw_input())

for case in range(num_cases):
    in_str = raw_input()
    data = in_str.split()
    data = map(lambda x: int(x), data)
    A = data[0]
    B = data[1]
    counter = 0
    for n in range(A, B):
        for m in range(n+1, B+1):
            if isRecycled(n,m):
                counter += 1
    print "Case #{0}: ".format(case+1) + str(counter) 