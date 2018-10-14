import sys
from collections import deque

def solve(R, k, groups):
    result = 0
    groups = deque(groups)
    for i in range(R):
        remain = k
        coaster = []
        while len(groups) > 0 and remain >= groups[0]:
            remain -= groups[0]
            result += groups[0]
            coaster.append(groups[0])
            groups.popleft()
        
        groups.extend(coaster)
    
    return result
        

def main():
    input = open(sys.argv[1])
    num = int(input.next())
    
    for i in range(num):
        R, k, N = [int(a) for a in input.next().split()]
        groups = [int(a) for a in input.next().split()]
        
        print 'Case #%d: %d' % (i + 1, solve(R, k, groups))
        
if __name__ == '__main__':
    main()
    
