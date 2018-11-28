in_data = open('C-large.in').readlines()
T=in_data[0]
in_data=in_data[1:]
outfile = open('result', 'w')
case_no = 0

def solve(a, b, digits):
    resdict = {}
    if digits == 1:
        return 0
    
    res = 0
    start = a
    end = b
    for i in range(1, digits):
        a = start
        b = end
        while a < b:
            sa = str(a)
            if sa[digits-i]=='0':
                a += 1
                continue
            front = sa[:(digits-i)]
            back = sa[(digits-i):digits]
            new = int(back+front)
            if new == a:
                a +=1
                continue
            if new > b:
                front = str(int(front)+1)
                back = '0' * len(back)
                a = int(front+back)
                continue
            if new > a:
                res +=1
                if a not in resdict:
                    resdict[a] = []
                resdict[a].append(i)
                a+=1
            else:
                a += 1
    for k,v in resdict.items():
        if len(v) == 1:
            continue
        out = set()
        k = str(k)
        for i in v:
            front = k[:(digits-i)]
            back = k[(digits-i):digits]
            new = int(back+front)
            out.add(new)
        res -= (len(v)-len(out))
    return res
            

for line in in_data:
    case_no += 1
    [a, b] = line.strip().split()
    digits = len(a)
    a = int(a)
    b = int(b)
    res = solve(a, b, digits)
    out = 'Case #' + str(case_no) + ': ' + str(res) + '\n'
    outfile.write(out)
    
outfile.close()