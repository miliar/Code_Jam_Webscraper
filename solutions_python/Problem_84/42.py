from sys import stdout

ifile = open('../input/A-large.in', 'r')
ofile = open('../output/A-large.out', 'w')
#ofile = stdout

cases = int(ifile.readline())

def fmt(c):
    if c == '1' or c == '4':
        return '/'
    if c == '2' or c == '3':
        return '\\'
    return c


def do():
    xs, ys = map(int, ifile.readline().split())
    result = []
    impossible = False
    for x in xrange(xs):    
        left = '.'    
        for c in ifile.readline().strip():
            try:
                top = result[-ys-1]
            except IndexError:
                top = '.'                                        
            if c == '.':
                if left == '1' or top == '1' or top == '2':
                    impossible = True 
                left = c
                result.append(left)
            else:             
                if top == '1':
                    left = '3'
                    result.append(left)
                elif left == '1':   
                    left = '2'     
                    result.append(left)
                elif left == '3':
                    left = '4'     
                    result.append(left)
                else:
                    left = '1'
                    result.append(left)
        if left == '1':
            impossible = True
        result.append('\n')
    lastline = result[-ys-1:] 
    if '1' in lastline or '2' in lastline:
        return None 
    if impossible:
        return None    
    return map(fmt, result)

for case in xrange(cases):
    result = do()
    if result:
        ofile.write('Case #%d:\n%s' % (case+1, ''.join(result)))
    else:
        ofile.write('Case #%d:\nImpossible\n' % (case+1))
    
        
        
    