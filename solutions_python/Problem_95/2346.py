mapping ={'a':'y','b':'h','c':'e','d':'s','e':'o','f':'c','g':'v','h':'x','i':'d','j':'u','k':'i','l':'g','m':'l','n':'b','o':'k','p':'r','q':'z','r':'t','s':'n','t':'w','u':'j','v':'p','w':'f','x':'m','y':'a','z':'q',' ':' '}

t = int(raw_input())
for i in range(1, t+1):
    s = raw_input()
    ans = ''
    for j in s:
        ans += mapping[j]
    print 'Case #%s: %s' % (i,ans)
