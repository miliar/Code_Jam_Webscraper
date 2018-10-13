import time
import math
starttime = time.time()

with open('B-large.in', 'r') as f:
    data_raw = f.readlines()
f.closed

def solve(input):
    l = max(input);
    best = l
    numbers = [0] * l
    for i in input:
        numbers[i - 1] += 1
    mx = 1
    while mx < best:
        i = mx
        sumSpecs = 0
        while i < l:
            i += 1
            v = numbers[i - 1]
            if v:
                sumSpecs += int((math.ceil(float(i) / mx) - 1)) * v
        if best > sumSpecs + mx:
            best = sumSpecs + mx
        mx += 1
    return best

data_raw = data_raw[::2][1:]
outputs = []
for line in data_raw:
    line = [int(x) for x in line.strip().split(' ')]
    outputs.append(solve(line))  

with open('B-large.out', 'w') as f:
    i = 1
    outputstrings= []
    for output in outputs:
        outputstrings.append('Case #{0}: {1}'.format(i, output))
        i += 1
    f.write('\n'.join(outputstrings))
f.closed

print time.time() - starttime