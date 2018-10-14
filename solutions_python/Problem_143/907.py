import sys
import collections

def main():
    file = sys.stdin
    lines = iter(file.readlines())

    testCase = int(lines.next())
   
    for caseNo in range(1, testCase+1):
        A, B, K = map(int, lines.next().lstrip().rstrip().split(' '))
        #print A, B, K
        result = 0
        for i in range(A):
            for j in range(B):
                
                combination = i & j
                if combination < K:
                    result += 1
        
        print 'Case #%d: %s'%(caseNo, result)            


if __name__ == '__main__':
    main()
   
