from datetime import datetime

input_file_path = 'A-large.in.txt'

start = datetime.now()

def compute(d,n,k,s):
    max = -1
    for i in range(0,n):
        time = float(d - k[i])/s[i]
        if time>max:
            max = time

    return float(d)/max

with open(input_file_path) as f:
    lines = f.read().splitlines()
    cases = int(lines[0])
    j=1
    case = 1
    while case<cases+1:
        d = int(lines[j].split(' ')[0])
        n = int(lines[j].split(' ')[1])
        k = []
        s = []
        for i in range(j+1,j+n+1):
            k.append(int(lines[i].split(' ')[0]))
            s.append(int(lines[i].split(' ')[1]))
        j = j+n+1
        output = compute(d,n,k,s)
        print 'Case #' + str(case) + ': ' + str(output)
        case = case+1


diff = datetime.now() - start
#print diff