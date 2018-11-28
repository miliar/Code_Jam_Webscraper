import math

in_data = open('A-large.in').readlines()
in_data = [x.strip() for x in in_data]
T = int(in_data[0])
in_data = in_data[1:]

def step(begin, m):
    if begin==1:
        return len(m)
    count = 0
    max_count = len(m)
    for i in range(len(m)):
        if begin > m[i]:
            begin += m[i]
            print(begin)
        else:
            max_count = min(max_count, count + (len(m)-i))
            tmp_count = int(math.log2((m[i]-1)/(begin-1)) + 1) + 1
            count += (tmp_count-1)
            print(tmp_count)
            begin = 2 ** (tmp_count - 1) * (begin - 1) + 1 + m[i]
            print(begin)
            if count > max_count:
                return max_count
    return count


wfile = open('result', 'w')
for case_no in range(T):
    dt = in_data[:2]
    in_data = in_data[2:]
    begin = int(dt[0].split()[0])
    m = [int(x) for x in dt[1].strip().split()]
    m.sort()
    res = step(begin, m)
    output = 'Case #' + str(case_no+1) + ': ' + str(res) + '\n'
    wfile.write(output)
    
wfile.close()
