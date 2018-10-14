import sys


def solve(input):
    chars = {}
    num = 0
    
    for c in input:
        if not c in chars:
            if num == 0:
                n = 1
            elif num == 1:
                n = 0
            else:
                n = num
            num += 1
            chars[c] = n
    
    if num < 2:
        num = 2
            
    keta = 0
    result = 0
    for c in reversed(input):
        result += chars[c] * num**keta
        keta += 1
        
    return result


def main():
    input = open(sys.argv[1])
    num_cases = int(input.readline())
    
    for i in range(num_cases):
        print 'Case #%d: %d' % (i+1, solve(input.readline().strip()))
    
        
if __name__ == '__main__':
    main()
    