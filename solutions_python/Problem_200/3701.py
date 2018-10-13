t = int(raw_input())
def is_tidy(s):
    s = str(s)
    l = len(s)
    for x in xrange(1, l):
        if not s[x - 1:x] <= s[x:x + 1]:
            return {'status':False,'x':x}
    return {'status': True}
for i in xrange(1,t+1):
    n = int(raw_input())
    init = is_tidy(n)
    if init['status']:
        print("Case #{}: {}".format(i, n))
    else:
        while True:
            s = str(n)
            l = len(s)
            x = init['x']
            s = s[:x - 1] + s[x - 1:x].replace(s[x - 1:x], str(int(s[x - 1:x]) - 1)) + ('9' * len(s[x:]))
            init = is_tidy(s)
            if init['status']:
                print("Case #{}: {}".format(i, int(s)))
                break
