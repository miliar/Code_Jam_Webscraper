import string

vowels = set(['a','e','i','o','u'])
consonants = set([c for c in string.ascii_lowercase if c not in vowels])

def get_substr(word, c):
    for i in range(len(word)):
        for x in range(i,len(word)+1):
            if x - i + 1 >= c:
                yield word[i:x]

def check_cons(_w, c):
    l = 0
    for ch in _w:
        if ch in consonants:
            l+=1
        else:
            if l >= c:
                return True
            else:
                l = 0
    return l >= c

def get_value(word, c):
    v = 0
    for substr in get_substr(word, c):
        v += 1 if check_cons(substr, c) else 0
    return v

input_file = 'Downloads/A-small-attempt0.in'

with open(input_file) as f:
    lines = f.readlines()
    cases = int(lines[0])
    for i in range(1,cases+1):
        line = lines[i]
        word, c = line.split(' ')
        c = int(c)
        v = get_value(word,c)
        print('Case #%s: %s' % (i,v))


