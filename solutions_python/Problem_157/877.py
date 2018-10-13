class Quaternion:
    type = '1'
    sgn = 1

    def __init__(self, t, s):
        self.type = t
        self.sgn = s

    def __str__(self):
        if self.sgn == -1:
            return '-' + self.type
        else:
            return self.type

def eval_q(a, b):
    if a.type == '1':
        return Quaternion(b.type, eval_sign(a, b))
    if a.type == 'i':
        if b.type == '1':
            return Quaternion(a.type, eval_sign(a, b))
        if b.type == 'i':
            return Quaternion('1', -1*eval_sign(a, b))
        if b.type == 'j':
            return Quaternion('k', eval_sign(a, b))
        if b.type == 'k':
            return Quaternion('j', -1*eval_sign(a, b))
    if a.type == 'j':
        if b.type == '1':
            return Quaternion(a.type, eval_sign(a, b))
        if b.type == 'i':
            return Quaternion('k', -1*eval_sign(a, b))
        if b.type == 'j':
            return Quaternion('1', -1*eval_sign(a, b))
        if b.type == 'k':
            return Quaternion('i', eval_sign(a, b))
    if a.type == 'k':
        if b.type == '1':
            return Quaternion(a.type, eval_sign(a, b))
        if b.type == 'i':
            return Quaternion('j', eval_sign(a, b))
        if b.type == 'j':
            return Quaternion('i', -1*eval_sign(a, b))
        if b.type == 'k':
            return Quaternion('1', -1*eval_sign(a, b))


def eval_sign(a, b):
    if a.sgn == 1:
        if b.sgn == 1:
            return 1
        else:
            return -1
    else:
        if b.sgn == 1:
            return -1
        else:
            return 1


def eval_str(s):
    total = Quaternion('1',1)
    for c in s:
        total = eval_q(total, Quaternion(c, 1))
    return total
# ijk

T = int(input())
for tc in range(T):
    inpt = input().split()
    L = int(inpt[0])
    X = int(inpt[1])
    inpt = X * input()
    rindexes = []
    lindexes = []
    rtotal = Quaternion('1', 1)
    ltotal = Quaternion('1', 1)
    for i in range(len(inpt)):
        c = inpt[i]
        q = Quaternion(c, 1)
        rtotal = eval_q(rtotal, q)
        if rtotal.type == 'i' and rtotal.sgn == 1:
            rindexes.append(i)

    for i in range(len(inpt)):
        i = len(inpt) - i - 1
        c = inpt[i]
        q = Quaternion(c, 1)
        ltotal = eval_q(q, ltotal)
        if ltotal.type == 'k' and ltotal.sgn == 1:
            lindexes.append(i)

    result = None
    if len(rindexes) > 0 and len(lindexes) > 0:
        rindex = rindexes[0]
        lindex = lindexes[0]
        if rindex < lindex:
            q = eval_str(inpt[rindex+1:lindex])
            if q.type == 'j' and q.sgn == 1:
                result = "YES"
            else:
                result = "NO"
        else:
            result = 'NO'
    else:
        result = "NO"
    if result is None:
        result = "NO"
    print("Case #" + str(tc+1) + ":", result)