n = int(raw_input())
dict = {'11':'1', '1i':'i',  '1j':'j', '1k':'k',
        'i1':'i', 'ii':'-1', 'ij':'k', 'ik':'-j',
        'j1':'j', 'ji':'-k', 'jj':'-1', 'jk':'i',
        'k1':'k', 'ki':'j', 'kj':'-i', 'kk':'-1'}

def mult2(s):
    cnt = 0
    while len(s)>1:
        news = ""
        for i in xrange(len(s)/2):
            w = mult(s[i*2], s[i*2+1])
            if w[0] == '-':
                cnt += 1
                w = w[1]
            news += w
        if len(s)%2==1:
            news += s[-1]
        s = news
    if cnt%2==1:
        s = '-'+s
    return s

def mult(s, t):
    w =''
    if len(s)==2:
        s = s[1]
        w += '-'
    key =s+t
    #print s, t, key, '->',
    w += dict[key]
    if len(w) == 3:
        w = w[2]
    #print  w
    return w


def output(s, l, x):
    str = s*x
    if len(set(s)) < 2 or not output2(s, l,x):
        return 'NO'
    s1 = "1"
    for i in xrange(0, l*x):
        s1 = mult(s1, str[i])
        if s1 !='i':
            continue
        s2 = "1"
        s3 = "1"
        for j in xrange(i+1, l*x):
            s2 = mult(s2, str[j])
            if s2 != 'j':
                continue
            else:
                s3 = mult2(str[j+1:])
                if s3 == 'k':
                    return 'YES'

    return 'NO'


def output2(s, l, k):
    if len(set(s)) < 2:
        return "NO"
    ans = mult2(s*x)
    if ans == '-1':
        return True
    return False



if __name__=='__main__':
    for i in xrange(n):
        l, x = map(int, raw_input().split())
        s = raw_input().strip()
        ret = output(s, l, x)
        print 'Case #%d: %s' % (i+1, ret)
