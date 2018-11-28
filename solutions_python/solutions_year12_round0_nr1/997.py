letters = {'a':'y', 'o':'e', 'z':'q'}

def modify_letters(g, s):
    i = 0
    while i < len(g):
        letters[g[i]] = s[i]
        i += 1

def decode(g):
    i = 0
    s = ''
    while i < len(g):
        s += letters[g[i]]
        i += 1
    return s

print(letters)
modify_letters("ejp mysljylc kd kxveddknmc re jsicpdrysi", "our language is impossible to understand")
print(letters)

f = open('training')

n = int(f.readline())

while n > 0:
    g = f.readline().strip()
    s = f.readline().strip()
    print('training g:', g, 'f', s)
    modify_letters(g, s)
    n -= 1

print('letter', letters)
print('num', letters.keys())
print('other', letters.values())

f = open('input')

n = int(f.readline())
tot = n
out = ""

while n > 0:
    out += "Case #%s: %s"%(tot-n+1,decode(f.readline().strip()))
    out += "\n"
    n -= 1

f = open('output', 'w')
f.write(out)
print(letters.values())
