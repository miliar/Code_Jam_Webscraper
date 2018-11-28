import sys

if len(sys.argv) != 3:
    print("Usage: python scriptA.py <input_file> <output_file>")
    exit()

input_file = sys.argv[1]
output_file = sys.argv[2]

#input_file = 'sampleA.in'
#output_file = 'sampleA.out'

results = []
with open(input_file, 'r') as f:
    T = int(f.readline())
    for t in xrange(T):
        r1 = int(f.readline())
        for i in xrange(4):
            line = f.readline()
            if i == r1 - 1: row1 = set(map(int,line.split()))

        r2 = int(f.readline())
        for i in xrange(4):
            line = f.readline()
            if i == r2 - 1: row2 = set(map(int,line.split()))

        s = row1.intersection(row2)
        res = 'Case #' + str(t+1) + ': '
        if len(s) == 1: res += str(list(s)[0])
        elif len(s) > 1: res += 'Bad magician!'
        else: res += 'Volunteer cheated!'
        res += '\n'
        results.append(res)

with open(output_file, 'w') as f:
        f.writelines(results)



