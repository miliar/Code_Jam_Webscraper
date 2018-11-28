import sys, os

file_in = 'B-small-attempt3.in'
file_out = 'B-small-attempt3.out'
#file_in = 'B-large.in'
#file_out = 'B-large.out'
#file_in = 'test.txt'
#file_out = 'test.out.txt'

f = open(file_in, 'r')
res_f = open(file_out, 'w')



def compute_result(s, combines, opposed):
    action_taken = False
    
    ret = ''
    if len(s) > 1:
        for a in s:
            if not ret:
                ret += a
                continue
            b = ret[-1]
            k = (min(a,b), max(a,b))
            if k in combines:
                ret = ret [:-1] + combines[k]
                action_taken = True
            else:
                if a in opposed and opposed[a] in ret:
                    ret = ''
                else:
                    ret += a
    else:
        ret = s
        
    return ret
    

line_num = 0
test_cases_num = 0

l = f.readline().strip('\n')
test_cases_num = int(l)
for i in range(test_cases_num):
    v = f.readline().strip('\n').split()
    n = int(v[0])
    combines = {}
    for a,b,c in v[1:n+1]:
        combines[(min(a,b), max(a,b))] = c
    v = v[n+1:]
    n = int(v[0])
    opposed = {}
    for a,b in v[1:n+1]:
        key = (min(a,b), max(a,b))
        opposed[a] = b
        opposed[b] = a
    
    v = v[n+2]
    
    res = compute_result(v, combines, opposed)

    print >> res_f, "Case #%s: [%s]" % ((i+1), ', '.join(list(res)))


try:
    f.close()
    res_f.close()
except:
    pass

print "done"