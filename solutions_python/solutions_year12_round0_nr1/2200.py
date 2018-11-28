tra = { 'a':'y','b':'h','c':'e','d':'s','e':'o','f':'c','g':'v','h':'x','i':'d','j':'u','k':'i','l':'g','m':'l',
        'n':'b','o':'k','p':'r','q':'z','r':'t','s':'n','t':'w','u':'j','v':'p','w':'f','x':'m','y':'a','z':'q'}
text = open('A-small-attempt0.in', 'r')
n = int(text.readline())
for i in range(0,n):
    line = text.readline()
    res = ''
    for char in line:
        if char not in tra:
            res += char
        else:
            res += tra[char]
    print 'Case #' + str(i+1) + ': ' + res
