out_file = open('output.txt', 'w')
cases = int(input())
for t in range(cases):
    line = input()
    pancakes = line.split()[0]
    size = int(line.split()[1])
    counter = 0
    
    for i in range(len(pancakes)):
        if pancakes[i] == '-' and i + size <= len(pancakes):
            counter += 1
            for j in range(i, i+size):
                if pancakes[j] == '-':
                    pancakes = pancakes[:j] + '+' + pancakes[j+1:]
                else:
                    pancakes = pancakes[:j] + '-' + pancakes[j+1:]
    if not '-' in pancakes:
        out_file.write('Case #' + str(t+1) + ': ' + str(counter) + '\n')
    else:
        out_file.write('Case #' + str(t+1) + ': IMPOSSIBLE\n')

out_file.close()
