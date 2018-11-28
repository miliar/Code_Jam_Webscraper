import time
with open('A-large.in', 'r') as f:
    data_raw = f.readlines()
f.closed

starttime = time.time()

data_raw = data_raw[1:]

outputs = []

def solve(input):
    output = 0
    currentmax = 0
    l = len(input)
    for i in xrange(l):
        n = int(input[i])
        if n > 0: 
            if i > currentmax:
                output += i - currentmax
                currentmax = i + n
            else:
                currentmax += n
            
    return output
    
for line in data_raw:
    line = line.strip().split(' ')
    outputs.append(solve(line[1]))  

with open('1.out', 'w') as f:
    i = 1
    outputstrings= []
    for output in outputs:
        outputstrings.append('Case #{0}: {1}'.format(i, output))
        i += 1
    f.write('\n'.join(outputstrings))
f.closed

print time.time() - starttime