import os

input_file = 'A-large.in'
out_file = input_file.replace('.in', '.out')
data = os.path.join(os.path.dirname(__file__), input_file)
data_o = os.path.join(os.path.dirname(__file__), out_file)

with open(data, 'r') as f:
    with open(data_o, 'w+') as ff:
        T = int(f.readline().strip('\n'))
        for i in range(1, T + 1):
            s, k = f.readline().strip('\n').split()
            s = list(s)
            k = int(k)
            res = 0
            start = 0
            n = len(s)
            while '-' in s:
                start = s.index('-')
                if len(s) - start < k:
                    res = 'IMPOSSIBLE'
                    break
                res += 1
                for j in range(start, start + k):
                    s[j] = '+' if s[j] == '-' else '-'
                s = s[start + 1:]
            ff.write('Case #%i: %s\n' % (i, res))
