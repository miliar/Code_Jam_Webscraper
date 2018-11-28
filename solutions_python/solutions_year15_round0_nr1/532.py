data = dict()
s_max = dict()
with open('A-large.in') as f:
    #lines = f.readlines()
    #print(f.readline())
    n_cases = int(f.readline().split()[0])
    for i in range(n_cases):
        line = f.readline().split()
        s_max[i] = int(line[0])
        data[i] = line[1]


def solve(smax, shystr):
    shy = [int(x) for x in list(shystr)]
    assert smax+1 == len(shy)
    n_needed = 0
    part_sum = [0] * (smax+1)
    part_sum[0] = shy[0]
    for i in range(1, smax+1):
        part_sum[i] = part_sum[i-1] + shy[i]
    #print(part_sum)
    for i in range(smax+1):
        if part_sum[i] < i+1:
            n_needed = max(n_needed, i+1 - part_sum[i])
        else:
            continue
    return n_needed

f = open('output_large.txt', 'w')
for i in range(n_cases):
    line = "Case #"+str(i+1)+": "+str(solve(s_max[i], data[i]))
    print(line)
    f.write(line+'\n')

f.close()

'''
solve(0, '8')
solve(1, '09')
solve(2, '009')
solve(10, '00100000001')
'''
