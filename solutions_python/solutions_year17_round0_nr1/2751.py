import sys 
sys.stdin.readline()
linenum = 1
def minflips(pancakes, k):
    flips = 0
    if k == 0:
        return 'IMPOSSIBLE'
    for pos in range(len(pancakes) - k + 1):
        if pancakes[pos] == '-':
            for curpancake in range(pos, pos + k):
                if pancakes[curpancake] == '-':
                    pancakes = pancakes[:curpancake] + '+' + pancakes[curpancake+1:]  
                else:
                    pancakes = pancakes[:curpancake] + '-' + pancakes[curpancake+1:]
            flips += 1
    if '-' not in pancakes:
        return flips 
    else:
        
        return 'IMPOSSIBLE'
        
for line in sys.stdin:
    print('Case #%d: ' % linenum, end = '')
    linenum += 1
    if line[-1] == '\n':
        print(minflips(line[:line.find(' ')], int(line[line.find(' ') + 1: -1])))
    else:
        print(minflips(line[:line.find(' ')], int(line[line.find(' ')+ 1:])))
    

      
        