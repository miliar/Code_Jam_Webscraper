def solve(s, k):
    cnt = 0
    for i in xrange(len(s)-(k-1)):
        if s[i] == '-':
            cnt += 1
            for j in range(i,i+k):
                if s[j] == '+':
                    s[j] = '-'
                else:
                    s[j] = '+'
    while i < len(s):
        if s[i] == '-':
            return "IMPOSSIBLE"
        i += 1
    return str(cnt)

    
        

    
f = open('A-Large.in')
#f = open('example.txt')
inputt = f.read()

f.close()
out = ''
l = inputt.splitlines()
cases = int(l[0])


for case in range(cases) :
    lines_per_case = 1
    lines = [l[1 + lines_per_case * case + i].split(' ') for i in range(lines_per_case)]

    s = [lines[0][0][i] for i in xrange(len(lines[0][0]))]
    k = int(lines[0][1])
    out += 'case #%d: %s' % (case+1, solve(s, k)) + '\n'

                            
#print inputt
print out
outfile = file('out', "w")
outfile.write(out)
outfile.close()
