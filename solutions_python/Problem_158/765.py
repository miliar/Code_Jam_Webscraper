import sys

def richard_wins(x, rc):
    if rc == 1 or rc == 3:
        return x > 1
    if rc == 2 or rc == 4 or rc == 8:
        return x > 2
    if rc == 6:        
        return x > 3
    if rc == 9:
        return x == 2 or x == 4
    if rc == 16:
        return x == 3
    return False

t = int(sys.stdin.readline().strip())
for case in range(1, t + 1):
    x, r, c = sys.stdin.readline().strip().split()
    print('Case #{}: {}'.format(case, 'RICHARD' if richard_wins(int(x), int(r)*int(c)) else 'GABRIEL'))