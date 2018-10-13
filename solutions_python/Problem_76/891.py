def choose(lst,n,allow_dup=True,distinguish_order=True):
    if allow_dup and distinguish_order:
        next = lambda lst, i: lst
    if allow_dup and not distinguish_order:
        next = lambda lst, i: lst[i:]
    if not allow_dup and not distinguish_order:
        next = lambda lst, i: lst[i+1:]
    if not allow_dup and distinguish_order:
        next = lambda lst, i: lst[:i]+lst[i+1:]

    def _choose(lst,n):
        if n == 0: return [[]]  # from ruby
        #if n == 1: return [[x] for x in lst]
        ans = []
        for i,x in enumerate(lst):
            ans.extend([[x]+l for l in _choose(next(lst,i),n-1)])
        return ans
    
    return _choose(lst,n)

def combination(lst,n=None):
    if n == None: n = len(lst)
    return choose(lst,n,allow_dup=False,distinguish_order=False)

def xor(seq):
    a = 0
    for i in seq:
        a = a ^ i
    return a

def remove(seq1, seq2):
    copy = seq2[:]
    for i in seq1:
        if i in copy:
            copy.remove(i)
    return copy

def calc(nums):
    big = 0
    for i in range(1, len(nums)):
        for c in combination(nums, i):
            tmp = remove(c, nums)
            """
            print c, tmp
            print xor(c), xor(tmp)
            """
            if xor(c) == xor(tmp):
                big = max(big, sum(c), sum(tmp))
                
    return big

lines = [i.rstrip() for i in open("C-small-attempt2.in", "r").readlines()]
size = (len(lines) - 1) / 2
case = 1
for i in range(size):
    idx = i * 2 + 2
    nums = [int(n) for n in lines[idx].split(" ")]
    ans = calc(nums)
    if ans == 0:
        print "Case #%d: NO" % case
    else:
        print "Case #%d: %d" % (case, ans)
    case += 1
        
