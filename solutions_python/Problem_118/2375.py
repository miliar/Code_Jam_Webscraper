from math import sqrt
def getCaseResult(instr, no):
    minstr, maxstr = instr.split(' ')
    min = int(minstr)
    max = int(maxstr)
    t1 = int(sqrt(min))
    if (t1*t1 >= min):
        m1 = t1
    elif (t1*t1 < min):
        m1 = t1+1
    t2 = int(sqrt(max))
    if (t2*t2 >= max):
        m2 = t2 + 1
    elif (t2*t2 < max):
        m2 = t2+1 
    count = 0
    #print no, min, max, m1, m2 
    for i in range (m1, m2):
        sum = i*i
        if check(sum):
            count = count + 1
            #print sum
    str_result = 'Case #%d: %d' % (no, count)
    return str_result

def check(num):
    if checkhw(num):
       t = sqrt(num)
       return checkhw(t)
    else:
       return False

def checkhw(num):
    s1 = '%d' % num
    rs = list(s1)
    rs.reverse()
    s2 = ''.join(rs)
    t = sqrt(num)
    if t > 10:
        return check(t)
    else:
        if (s1 == s2):
           return True
        else:
            return False
    

all_lines = open('2.in','r').readlines()
total = int(all_lines[0])
allcases = {}
count = 1
for line in all_lines[1:]:
    allcases[count] = line[:-1]
    count = count + 1

r_list = []
for num, instr in allcases.iteritems():
    str_result = getCaseResult(instr, num)
    r_list.append(str_result)
    print str_result
    
open('2.out','w').write('\n'.join(r_list))