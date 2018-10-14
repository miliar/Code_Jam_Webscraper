
def get_int():
    return int(get_word())

def get_word():
    if not 'words' in dir(get_word):
        get_word.words=[]
    while len(get_word.words)==0:
        get_word.words=raw_input().split()
    return get_word.words.pop(0)


def snap(t):
    nt = ''
    enough = False
    for c in t:
        if enough:
            nt+=c
            continue
        nt += c.swapcase()
        if c.islower():
            enough = True
    return nt

def test(n, k):
    t = 'a'*n
    for i in range(k):
        t = snap(t)
    return t.isupper()

for i in range(get_int()):
    print 'Case #'+str(i+1)+': ' + (test(get_int(),get_int())and 'ON' or 'OFF')

