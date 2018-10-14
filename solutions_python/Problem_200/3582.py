# Yash Mittal [yashmittal2009@gmail.com]


def func(n):
    strN = str(n)
    for i in range(len(strN) - 1):
        if strN[i] <= strN[i + 1]:
        	pass
        elif (i <= len(strN) - 2):
        	sub = (n % (10 ** (len(strN) - i - 1))) + 1
        	return func(n - sub)
    return n


with open('B-large.in', 'r') as fin:
    with open('output.out', 'w') as fout:
        t = int(fin.readline())
        for i in range(1, t + 1):
            line = fin.readline().strip()
            result = func(int(line))
            fout.write('Case #{}: {}\n'.format(i, result))
