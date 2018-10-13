INPUT_FILE = 'B-large.in'
OUTPUT_FILE = 'B-large_out.txt'


def helper(n):
    for index in range(len(n) - 1):
        if n[index] > n[index + 1]:
            if n[index] == 0:
                for iid, sec in enumerate(n[index::-1]):
                    if sec != 0:
                        n[sec] -= 1
                        j = sec + 1
                        break
                    else:
                        if iid == 0:
                            del n[0]
                            j = 0
                            break
            else:
                n[index] -= 1
                j = index + 1
            for dig in range(j, len(n)):
                n[dig] = 9
            helper(n)
            break
    return n


def solve(n):
    n = str(n)
    n = list(n)
    del(n[len(n) - 1])
    for p in range(len(n)):
        n[p] = int(n[p])
    if len(n) == 1:
        n = int(n[0])
    else:
        n = helper(n)
        n = int(''.join(map(str, n)))

    return n


with open(INPUT_FILE, 'r') as f:
	with open(OUTPUT_FILE, 'w') as f_out:
		T = int(f.readline())
		for i in range(T):
			f_out.write('Case #%d: %s\n' % (i + 1, solve(f.readline())))