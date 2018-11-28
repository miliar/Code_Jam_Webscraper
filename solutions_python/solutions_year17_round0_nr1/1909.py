

k = int(raw_input())

all_data = []
for i in range(k):
    s = raw_input().split()
    s[0] = [True if j=='+' else False for j in list(s[0])]
    s[1] = int(s[1])
    all_data.append(s)


flip = lambda sub_s: [not i for i in sub_s]
def cal(process_s, k):
    record = [process_s[0][0]]
    while process_s:
        f_s, count = process_s.pop(0)
        if all(f_s):
            return count
        for i in range(len(f_s) -k +1):
            s_s = f_s[:]
            s_s[i: i+k] = flip(f_s[i: i+k])

            if s_s not in record:
                record.append(s_s)
                process_s.append([s_s, count + 1])
            else:
                continue

for i in range(len(all_data)):
    r = cal([[all_data[i][0], 0]], all_data[i][1])
    if r == None:
        r = 'IMPOSSIBLE'
    
    print 'Case #{0}: {1}'.format(i+1, r)
