class BIT(object):
    def __init__(self, arr):
        self.n = len(arr) + 1
        self.bit = [0]*self.n
        for i in range(self.n-1):
            self.update(i, arr[i])

    def _update(self, ind, val):
        if ind >= self.n:
            return
        self.bit[ind] += val
        # ind + number with only last '1' in ind
        ind = ind + ( ind & -ind)
        self._update(ind, val)

    def update_range(self, ind1, ind2, val):
        self._update(ind1+1, val)
        self._update(ind2+2, val)

    def update(self, ind, val):
        self.update_range(ind, ind, val)

    def _get_sum(self, ind):
        if ind <= 0 : return 0
        # ind - number with only last '1' in ind
        return self.bit[ind] + self._get_sum(ind - ( ind & -ind) )

    def get_value(self, ind):
        ind += 1
        return self._get_sum(ind)

    def pr(self):
        print(self.bit)

s = str(raw_input(""))
t = int(s)
for case in range(t):
    s = str(raw_input(""))
    s = s.split(' ')
    s,k = s[0],int(s[1])
    s = [0 if x is '-' else 1 for x in s]
    n = len(s)
    bit = BIT(s)
    ans = 0
    tries = 2000
    alldone = False
    i = 0
    while tries > 0 and not alldone :
        tries -= 1
        alldone = True 
        while i < n: 
            if bit.get_value(i) % 2  == 0:
                alldone = False
                break
            i += 1
        if alldone: break
        ans += 1
        if i + k - 1 >= n:
            i = i - (i+k-n)
        bit.update_range(i, i+k-1, 1)
        #print([ '+' if bit.get_value(j) % 2 else '-' for j in range(n) ])

    s = [ '+' if bit.get_value(j) % 2 else '-' for j in range(n) ]

    if '-' in s:
        ans = "IMPOSSIBLE"
    print("Case #%d: %s" % (case+1, ans))



