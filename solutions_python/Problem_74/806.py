# Problem A: Bot Trust
from Bot import Bot

def read_input(path="a-sample.txt"):
    '''
    Read in, process and return the input from the given file.
    '''
    input = open(path).readlines()[1:]
    
    proc = []
    for line in input:
        line = line.split()
        line_len = int(line[0])
        line = line[1:]
        line = [(line[2*n], line[2*n+1]) for n in xrange(line_len)]
        proc.append(line)
    return proc
    
def solve(proc, debug=False):
    '''
    Solve the problem for the given processed input.
    '''
    results = []
    out_file = open('a-results.txt', 'wb')
    case = 1
    for line in proc:
        time = 0
        #print "BEGIN CASE", case
        o = Bot('O', debug=debug)
        b = Bot('B', debug=debug)
        o.take_input(line)
        b.take_input(line)
        
        cursor = 0
        while not (o.complete and b.complete):
            p = line[cursor]
            o.active = p[0] == 'O'
            b.active = p[0] == 'B'
            
            if o.tick() and o.active:
                cursor += 1
            if b.tick() and b.active:
                cursor += 1
                
            time += 1
                
        r = 'Case #%d: %d' % (case, time)
        out_file.write(r+'\r\n')
        print r
        case += 1
    out_file.close()
        
if __name__ == '__main__':
    solve(read_input('A-large.in'))