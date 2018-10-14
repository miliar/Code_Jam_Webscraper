def do(inp):
        lines = inp.split('\n')
        T = int(lines[0])
        cases = lines[1:]
        result = ""
        for i in range(T):
                line = cases[i]
                n,k = map(int,line.split(' '))
                answer =  "ON" if k % (2**n)==2**n-1 else "OFF"
                result += "Case #%s: %s\n" % (str(i+1),answer)
        return result
        
if __name__ == '__main__':
    filename = 'A-large'   
    inp = open('%s.in' % filename).read()
    r = do(inp)
    open('%s.out' % filename,'w').write(r)

