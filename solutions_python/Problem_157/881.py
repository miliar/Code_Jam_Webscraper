from sys import stdin

def _other(x, y):
    return [u for u in ('i', 'j', 'k') if u not in (x, y)][0]

def _mult(x, y):
    if x == 1:
        return (1, y)
    elif y == 1:
        return (1, x)
    elif x == y:
        return (-1, 1)
    else:
        sign = 1 if (ord(y) - ord('i')) % 3 == (ord(x) - ord('i') + 1) % 3 else -1
        vector = _other(x, y)
        return (sign, vector)

basis = (1, 'i', 'j', 'k')
mult = { (x, y): _mult(x, y) for x in basis for y in basis }

class quaternion:
    def __init__(self, sign, vector):
        self.sign = sign
        self.vector = vector

    def mult(self, q):
        sign, vector = mult[(self.vector, q.vector)]
        self.sign = self.sign * sign * q.sign
        self.vector = vector

    def __str__(self):
        if self.sign > 0:
            return str(self.vector)
        else:
            return '-' + str(self.vector)

def simplify(prod):
    result = quaternion(1, 1)
    for c in prod:
        result.mult(quaternion(1, c))
    return result

def solve(ijks, x):
    cur = quaternion(1, 1)
    target = 'i'
    for _ in range(x):
        for c in ijks:
            cur.mult(quaternion(1, c))
            if cur.sign == 1 and cur.vector == target:
                target = chr(ord(target) + 1)
                cur = quaternion(1, 1)
    if target == 'l' and cur.sign == 1 and cur.vector == 1:
        return 'YES'
    else:
        return 'NO'

if __name__ == '__main__':
    ncases = int(stdin.readline())
    for i in range(ncases):
        [l, x] = [int(x) for x in stdin.readline().split()]
        ijks = stdin.readline().strip()
        result = solve(ijks, x)
        print("Case #{}: {}".format(i + 1, result))
