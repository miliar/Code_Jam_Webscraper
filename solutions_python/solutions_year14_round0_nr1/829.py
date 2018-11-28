def bla(a,b):
    res = set(a).intersection(set(b))
    if len(res) == 0:
        return 'Volunteer cheated!'
    elif len(res) == 1:
        return str(list(res)[0])
    else:
        return 'Bad magician!'

f = map(str.strip,open('A-small-attempt0.in'))

case = 1
i = 1
while i < len(f):
    a = map(int,f[i+int(f[i])].split())
    i += 5
    b = map(int,f[i+int(f[i])].split())
    i += 5
    print 'Case #%d:'%case, bla(a,b)
    case += 1
