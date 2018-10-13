inputFile = 'A-large.in'

with open(inputFile, 'r') as f:
    rawInput = f.readlines()
    
print(rawInput)

numTestCases = int(rawInput[0].strip())
numTestCases

def reduce(pancakes):
    for i, _ in enumerate(pancakes):
        if pancakes[i] != '+':
            return pancakes[i:]

def flip_firsts(pancakes, K):
    for i in range(K):
        if pancakes[i] == '-':
            pancakes = pancakes[0:i] + '+' + pancakes[i+1:]
        else:
            pancakes = pancakes[0:i] + '-' + pancakes[i+1:]
    return pancakes
        
for i in range(1, numTestCases+1):
    
    parts = rawInput[i].split()
    
    K = int(parts[1])
    pancakes = parts[0]
    
    flips = 0
    
    pancakes = reduce(pancakes)
    if pancakes == None:
        print('Case #{}: {}'.format(i, flips))
        continue
    
    printed = False
    while(len(pancakes) >= K):
        flips += 1
        pancakes = reduce(flip_firsts(pancakes, K))
        if pancakes == None:
            print('Case #{}: {}'.format(i, flips))
            printed = True
            break
    
    if printed:
        continue
        
    print('Case #{}: {}'.format(i, 'IMPOSSIBLE'))
    
    