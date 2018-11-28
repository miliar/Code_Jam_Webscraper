import sys

def match(s, n):
    c, t, sign = -1, 0, 1
    for i in xrange(n):
        v = s[i]
        if c == -1:
            c = v
        elif c == v:
            c = -1
            sign = -sign
        elif v == (c + 1) % 3:
            c = (c + 2) % 3
        else:
            c = (c + 1) % 3
            sign = -sign
        
        if t < 2 and c == t:
            t += 1
            c = -1
    
    if c == 2 and t == 2 and sign == 1:
        return True
    else:
        return False

if __name__ == '__main__':
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    with open(output_file, 'w') as output:
        with open(input_file, 'r') as input:
            T = int(input.readline())
            for i in xrange(T):
                l, x = map(int, input.readline().split())
                s = input.readline().strip()
                a = []
                for c in s:
                    a.append(ord(c) - ord('i'))
                rst = match(a * x, x * l)
                if rst:
                    output.write("Case #%d: %s\n" %(i+1, 'YES'))
                else:
                    output.write("Case #%d: %s\n" %(i+1, 'NO'))