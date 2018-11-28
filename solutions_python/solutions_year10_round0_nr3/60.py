def solve2(R, k, q):
    _sum = 0
    i=0
    for x in range(R):
        _group = []
        while True:
            _sg = sum(_group)
            if (_sg+q[i])>k or len(_group)==len(q):
                _sum = _sum+_sg
                _group=[]
                break
            else:
                _group.append(q[i])
                i=(i+1)%len(q)
    return _sum

def solve(R, k, q):
    i=0
    _key=''
    _sum=0
    _l = []
    _d = dict()
    len_q = len(q)
    key_len=0
    repeat = False
    while True:
        if (_sum+q[i])>k or key_len>=len_q:
            if repeat==True and _key in _d:
                break
            else:
                _l.append((_key, _sum))
                _d[_key]=len(_l)-1
                _sum=0
                _key=''
                key_len=0
                if len(_l)>=R:
                    return sum([x[1] for x in _l])
        else:
            _key=_key+','+str(q[i])+'-'+str(i)
            _sum=_sum+q[i]
            i=(i+1)%len_q

            if repeat==False and i==0:
                repeat=True
                
            key_len=key_len+1
            
    
    i = _d[_key]
    sec = len(_l) - i
    sum_sec_t = (R-i)//sec
    sum_sec = sum(x[1] for x in _l[i:]) * sum_sec_t
    sum_sec_m = (R-i)%sec
    ans = sum(x[1] for x in _l[0:i]) + sum_sec + sum(x[1] for x in _l[i:i+sum_sec_m])
    
    return ans

#print(solve(68, 10, [8,6,7,7,9,7,8,5]))
#print(solve2(68, 10, [8,6,7,7,9,7,8,5]))


fin = open('C-large.in', 'r')
fout = open('out.txt', 'w')
nc = int(fin.readline().rstrip())
for i in range(1,nc+1):
    (R, k, _) = [int(s) for s in fin.readline().rstrip().split()]
    q = [int(s) for s in fin.readline().rstrip().split()]
    fout.write('Case #%d: %d\n'%(i, solve(R, k, q)))
    
fin.close()
fout.close()
