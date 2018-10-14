import sys

def case_iterator(path):
    with file(path) as f:
        lines = iter(f)
        n = int(lines.next())
        
        for i in range(1, 1 + n):
            yield i, read_case(lines)
    
def read_case(lines):
    x, s, r, t, n = [int(i) for i in lines.next().split()]
    walkways = [[int(y) for y in lines.next().split()] for _ in xrange(n)]
    return x, s, r, t, walkways 
    
def solve(case):
    x, s, r, t, walkways = case
    total_walkway = sum([y[1] - y[0] for y in walkways])
    regular = x - total_walkway
    parts = [(y[1] - y[0], y[2] + s) for y in walkways]
    parts.append((regular, s))
    running = []
    def key(x):
        return x[1]
    
    parts = sorted(parts, key=key)
    
    while parts and t > 0:
        part = parts.pop(0)
        speed = part[1] + r - s
        if speed * t >= part[0]:
            t -= float(part[0]) / speed
            running.append((part[0], speed))
        else:
            running.append((speed * t, speed))
            parts.append((part[0] - speed * t, part[1]))
            t = 0
    
    time = 0
    for part in parts + running:
        time += float(part[0]) / part[1]
    
    return str(time)
        
           
    
def main():
    try:
        path, = sys.argv[1:]
    except ValueError:
        sys.exit('usage: %s <input file>' % (sys.argv[0],))
    
    for i, case in case_iterator(path):
        print 'Case #%d: %s' % (i, solve(case))
        

if __name__ == '__main__':
    main()
