def is_tidy(n):
    p = 10
    while n:
        c = n % 10
        if c <= p:
            p = c
            n //= 10
        else:
            return False

    return True

def solve(n):
    for i in range(n, 0, -1):
        if is_tidy(i):
            return i



from pathlib import Path
import sys

from tqdm import trange

def main():
    ip = sys.argv[1]
    lines = (l.strip() for l in open(ip))
    t = int(next(lines))
    
    cases = (int(l) for l in lines)

    with open(Path(ip).with_suffix('.out').name, mode='w') as op:
        for i in trange(t):
            case = next(cases)
            r = solve(case)
            print(f'Case #{i+1}: {r}', file=op)

main()
