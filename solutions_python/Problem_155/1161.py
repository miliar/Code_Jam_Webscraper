import sys

def invited(a, n):
    num = 0
    total = 0
    for i in xrange(n+1):
        if total + num < i:
            num += i - total - num
        total += a[i]
    return num

if __name__ == '__main__':
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    with open(output_file, 'w') as output:
        with open(input_file, 'r') as input:
            T = int(input.readline())
            for i in xrange(T):
                maxS, line = input.readline().strip().split()
                maxS = int(maxS)
                a = []
                for c in line:
                    a.append(int(c))
                num = invited(a, maxS)
                output.write("Case #%d: %d\n" %(i+1, num))