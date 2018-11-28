def get_digit(n):
    d = dict()
    for i in range(1, 10):
        d[i] = 0
    for i in str(n):
        i = int(i)
        if i == 0:
            continue
        d[i] += 1
    
    return d

def comp(d1, d2):
    for i in range(1, 10):
        if d1[i] != d2[i]:
            return False
        
    return True

def next(n):
    ori_digit = get_digit(n)
    while True:
        n += 1
        new_digit = get_digit(n)
        if comp(ori_digit, new_digit):
            return n
        
def main(f, out='result.txt'):
    rfile = open(f)
    rfile.readline()
    case = 1
    wfile = open(out, 'w')
    for line in rfile:
        n = line.strip()
        n = next(int(n))
        wfile.write('Case #'+str(case)+': '+str(n)+'\n')
        case += 1
        print case
        
        
if __name__ == '__main__':
    import sys
    import psyco
    psyco.full()
    in_file = sys.argv[1]
    
    main(in_file)
    