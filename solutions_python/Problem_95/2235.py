case_prefix = 'Case #'


d = {' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q'}

f = open('A-small-attempt0.in', 'r')
num_tests = int(f.readline().strip())
for case in range(num_tests):
    line = f.readline().strip()
    s = str(case_prefix) + str(case + 1) + ': '
    for c in line:
        s += d[c]
    print s
f.close()
