def dance(n,s,p,t):
    surprising_num = 0
    not_surprising_num = 0
    for ti in t:
        if ti >= 3*p - 2:
            not_surprising_num += 1
        elif ti >= 3*p - 4 and ti!=0:
            surprising_num += 1
    return not_surprising_num + min(surprising_num, s)

f = open('B-large.in')
f_out = open('B-large.out','w')
num_of_cases = int(f.readline())
for i in range(1,num_of_cases+1):
    s = f.readline()
    numbers = [int(x) for x in s.split()]
    n = numbers[0]
    s = numbers[1]
    p = numbers[2]
    t = numbers[3:]
    result = dance(n,s,p,t)
    res = 'Case #%d: %s\n' % (i,result)
    f_out.write(res)
f.close()
f_out.close()
