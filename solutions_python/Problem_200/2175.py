def boilerplate(filename):
    with open(filename, 'r') as infi:
        with open('output-'+filename, 'w') as outfi:
            numcases = infi.readline().strip()
            numcases = int(numcases)
            for i in range(numcases):
                case = infi.readline().strip()
                outfi.write(f(i, case)+'\n')

def tester(x):
    return f(x, x)

def tidynumbers(casenumber, inp):
    def helper(x):
        x = str(x)
        if x == '0':
            return '0'
        biggest, bigindex = 0, -1
        sofar = '0'
        for i in range(len(x)):
            if int(x[i]) < biggest:
                sofar = helper(int(sofar) - 1)
                sofar += '9' * (len(x) - i)
                return sofar
            else:
                sofar += x[i]
                biggest, bigindex = int(x[i]), i
        return sofar

    return 'Case #%s: %s' % (casenumber+1, int(helper(inp)))


f = tidynumbers
