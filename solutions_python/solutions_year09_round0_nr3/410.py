import sys

def build_positions(base, line):
    positions = {}
    for i, c in enumerate(line):
        if c in base:
            if not c in positions:
                positions[c] = []

            positions[c].append(i + 1)
    return positions

def count_subsequences(base, line):
    base_positions = build_positions(base, base)
    unique = set(base_positions.keys())
    
    counts = [1] + [0 for c in base]    
    for c in line:
        if c in unique:  
            for position in base_positions[c]:
                counts[position] += counts[position - 1]
    return counts[len(base)]

base = "welcome to code jam"
test_cases = int(sys.stdin.readline().strip())
for test_case in range(test_cases):
    line = sys.stdin.readline().strip()
    print "Case #" + str(test_case + 1) + ": " + ("%04d" % count_subsequences(base, line))[-4:]