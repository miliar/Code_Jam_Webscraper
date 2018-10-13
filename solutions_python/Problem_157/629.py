T = int(input())

class Quaternion(object):
    def __init__(self, val='0', one=0, i=0, j=0, k=0):
        self.one = one
        self.i = i
        self.j = j
        self.k = k

        if val not in ('1', 'i', 'j', 'k', '0'):
            raise ValueError('Initial values can only be one dimensional unit vectors or zero')

        minus = 1
        if val.startswith('-'):
            minus = -1
            val = val[1:]

        if val == '1':
            self.one += minus
        elif val == 'i':
            self.i += minus
        elif val == 'j':
            self.j += minus
        elif val == 'k':
            self.k += minus

    def __add__(self, other):
        one = self.one + other.one
        i = self.i + other.i
        j = self.j + other.j
        k = self.k + other.k
        return Quaternion(one=one, i=i, j=j, k=k)

    def __neg__(self, other):
        return Quaternion(one=-self.one, i=-self.i, j=-self.j, k=-self.k)

    def __mul__(self, other):
        one = self.one * other.one - self.i * other.i - self.j * other.j - self.k * other.k
        i = self.one * other.i + self.i * other.one + self.j * other.k - self.k * other.j
        j = self.one * other.j + self.j * other.one - self.i * other.k + self.k * other.i
        k = self.one * other.k + self.k * other.one + self.i * other.j - self.j * other.i
        return Quaternion(one=one, i=i, j=j, k=k)

    def __str__(self):
        vals = []
        if self.one != 0:
            vals.append(str(self.one))
        if self.i != 0:
            vals.append(str(self.i) + 'i')
        if self.j != 0:
            vals.append(str(self.j) + 'j')
        if self.k != 0:
            vals.append(str(self.k) + 'k')

        return ' + '.join(vals)

    def __repr__(self):
        return '<Quaternion: {} + {}i + {}j + {}k>'.format(self.one, self.i, self.j, self.k)

    def __eq__(self, other):
        if self.one != other.one:
            return False
        if self.i != other.i:
            return False
        if self.j != other.j:
            return False
        if self.k != other.k:
            return False
        return True

    def __ne__(self, other):
        return not self.__eq__(other)

one = Quaternion('1')
i = Quaternion('i')
j = Quaternion('j')
k = Quaternion('k')

for t in range(T):
    #print(t)
    L, X = map(int, input().split())

    s = input() * X

    if L*X < 3:
        print('Case #{}: NO'.format(t+1))
        continue

    good = False

    leftind = 0
    lq = Quaternion('1')
    for left in range(L*X-2):
        #print('left = {}, {}'.format(left, s[:left+1]))
        #print('left = {}'.format(left))
        lq = lq * Quaternion(s[left])
        if lq == i:
            #print('  yes')
            leftind = left + 1
            break
    else:
        print('Case #{}: NO'.format(t+1))
        continue


    rightind = []
    rq = Quaternion('1')
    for right in range(L*X-1, 1, -1):
        #print('right = {}, {}'.format(right, s[right:]))
        #print('right = {}'.format(right))
        rq = Quaternion(s[right]) * rq
        #print('  q = {}'.format(repr(rq)))
        if rq == k:
            #print('  yes')
            rightind = right
            break
    else:
        print('Case #{}: NO'.format(t+1))
        continue

    #print('left: {}'.format(s[:leftind]))
    #print('mid: {}'.format(s[leftind:rightind]))
    #print('right: {}'.format(s[rightind:]))

    mq = Quaternion('1')
    for mid in range(leftind, rightind):
        mq = mq * Quaternion(s[mid])
        #print(mid, s[mid], mq)


    if mq == j:
        print('Case #{}: YES'.format(t+1))
    else:
        print('Case #{}: NO'.format(t+1))

