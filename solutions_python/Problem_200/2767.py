def solve(s):
    spot = len(s)
    for i in range(len(s)-2, -1, -1):
        if s[i] > s[i+1]:
            spot = i+1
            s[i] -= 1
    res = ""
    wasnot0 = False
    for i in range(spot):
        if wasnot0 == False and s[i] == 0:
            continue
        wasnot0 = True
        res += str(s[i])
    res += "9"*(len(s)-spot)
    return res
    
      
def main():
    f = open('B-large.in')
    #f = open('example.txt')
    inputt = f.read()
    
    f.close()
    out = ''
    l = inputt.splitlines()
    cases = int(l[0])


    for case in range(cases) :
        lines_per_case = 1
        lines = [l[1 + lines_per_case * case + i].split(' ') for i in range(lines_per_case)]
    
        s = [int(lines[0][0][i]) for i in xrange(len(lines[0][0]))]
        out += 'Case #%d: %s' % (case+1, solve(s)) + '\n'

                            
    #print inputt
    print out
    outfile = file('out', "w")
    outfile.write(out)
    outfile.close()


main()
