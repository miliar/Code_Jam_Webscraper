import sys

if len(sys.argv) != 3:
    print("Usage: python scriptB.py <input_file> <output_file>")
    exit()

input_file = sys.argv[1]
output_file = sys.argv[2]

#input_file = 'sampleA.in'
#output_file = 'sampleA.out'

def extract_max_horiz(pattern, N, M):
    result = []
    for row in xrange(0,N):
        result.append(max(pattern[row]))
    return result

def extract_max_vert(pattern, N, M):
    result = []
    for col in xrange(0,M):
        max_val = 0
        for row in xrange(0,N):
            if max_val < pattern[row][col]: max_val = pattern[row][col]
        result.append(max_val)
    return result

def check_pattern(pattern, N, M):
    rows = extract_max_horiz(pattern, N, M)
    cols = extract_max_vert(pattern, N, M)
    for row in xrange(0,N):
        for col in xrange(0,M):
            if pattern[row][col] != rows[row] and pattern[row][col] != cols[col]:
                return 0
    return 1

results = []
with open(input_file, 'r') as f:
    T = int(f.readline())
    for c in xrange(0,T):
        line = f.readline()
        N, M = tuple(map(int, line.split(' ')))
        pattern = []
        for row in xrange(0,N):
            line = f.readline()
            pattern.append(map(int,line.split(' ')))

        if check_pattern(pattern, N, M):
            results.append('Case #' + str(c+1) + ': YES\n')
        else: results.append('Case #' + str(c+1) + ': NO\n')

with open(output_file, 'w') as f:
        f.writelines(results)



