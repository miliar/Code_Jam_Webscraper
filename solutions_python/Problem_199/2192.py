numCases = int(input())
for i in range(1, numCases+1):
    line = input().split(' ')
    pancakes = list(line[0])
    size = int(line[1])

    count = 0
    
    if ('+' in pancakes and '-' not in pancakes):
        output = "Case #%d: %d" % (i, count)
    elif size > len(pancakes):
        output = "Case #%d: IMPOSSIBLE" % i
    else:
        for j in range(len(pancakes)-(size-1)):
            if pancakes[j] == '-':
                count += 1
                for k in range(size):
                    if pancakes[j+k] == '-':
                        pancakes[j+k] = '+'
                    else:
                        pancakes[j+k] = '-'
                        
                
        
        if ('+' in pancakes and '-' not in pancakes):
            output = "Case #%d: %d" % (i, count)
        else:
            output = "Case #%d: IMPOSSIBLE" % i

    print(output)