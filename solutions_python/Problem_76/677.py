import sys
import itertools

lines = sys.stdin.readlines()
lines = map(lambda a:a.rstrip('\n'), lines)
#print lines

T = int(lines[0])
for i in range(T):
    T = int(lines[i*2+1])
    data = lines[i*2+2].split()
    v_list = map(lambda a:format(int(a), 'b'), data)
    
    def _add(v1, v2):
        l1 = len(v1)
        l2 = len(v2)
        if l1>l2:
            v2 = '0'*(l1-l2) + v2
        elif l1<l2:
            v1 = '0'*(l2-l1) + v1
        #print v1, v2
        ans = ''
        for i in range(len(v1)):
            if v1[i]==v2[i]:
                ans += '0'
            else:
                ans += '1'
        #print ans
        #return int(ans, 2)
        return ans
    
    max_value = -1
    for j in range(1, len(v_list)):
        for index_list in itertools.combinations(range(len(v_list)), j):
            #print index_list
            sum_inlist = 0
            sum_normal = 0
            sum_binary = '0'
            for k in range(len(v_list)):
                if k in index_list:
                    sum_inlist += int(v_list[k], 2)
                else:
                    sum_normal += int(v_list[k], 2)
                    sum_binary = _add(sum_binary, v_list[k])
            if sum_inlist==int(sum_binary, 2):
                if max_value<sum_normal:
                    max_value = sum_normal
                    
    if max_value==-1:
        print 'Case #%d: NO' % (i+1)
    else:
        print 'Case #%d: %d' % (i+1, max_value)
        