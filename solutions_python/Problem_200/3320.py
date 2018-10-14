
def solve(n):
    n = [int(c) for c in str(n)]
    l = len(n)
    for i in range(1, l):
        if n[i] < n[i-1]:
            for j in range(i, l):
                n[j] = 9
            n[i-1] -= 1
            k = i-1
            while k > 0:
                if n[k] < 0:
                    n[k-1] -= 1
                    n[k] = 9
                elif n[k] < n[k-1]:
                    n[k-1] = n[k]
                    n[k] = 9
                k -= 1 
            break
    if n[0] == 0:
        n = [9]*(len(n) - 1)
    return str(int(''.join([str(c) for c in n])))


if __name__ == "__main__":
    output = []
    fname = 'B-large'
    with open(fname + '.in') as f:
        inputs = [line.strip() for line in f]
    for i in range(1, len(inputs)):
        n = inputs[i]
        output.append("Case #%d: " % i + solve(n))

    with open(fname + '.out', 'w') as f:
        f.write('\n'.join(output))

"""
# CODE TO TEST MY METHOD

def is_tidy(n):
    n = [int(c) for c in str(n)]
    for i in range(1, len(n)):
        if n[i] < n[i-1]:
            return False
    return True

for i in range(1, 1000000):
    if is_tidy(i):
        last_tidy = str(i)
    assert solve(i) == last_tidy
"""