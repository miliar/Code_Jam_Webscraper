import sys

if len(sys.argv) != 3:
    print("Usage: python scriptB.py <input_file> <output_file>")
    exit()

input_file = sys.argv[1]
output_file = sys.argv[2]

def find_min_time(S, C, F, X):
    min_time = X / S
    curr_time = 0
    while curr_time < min_time:
        curr_time += C / S
        S += F
        if min_time > curr_time + X / S:
            min_time = curr_time + X / S
    return min_time

results = []
with open(input_file, 'r') as f:
    T = int(f.readline())
    for t in xrange(T):
        line = f.readline()
        C, F, X = tuple(map(float, line.split(' ')))
        fin = find_min_time(2, C, F, X)
        results.append('Case #%d: %.7f\n' % (t+1,fin))

with open(output_file, 'w') as f:
        f.writelines(results)

