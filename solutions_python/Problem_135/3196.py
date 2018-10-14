'''
Created on Apr 13, 2012

@author: yonch
'''

d = {' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q'}

def eat(lines):
    return lines[0], lines[1:]
 
def do(l):
    return ''.join(map(lambda x: d[x], l))

def read():
    return """3
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
3
1 2 5 4
3 11 6 15
9 10 7 12
13 14 8 16
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
3
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16""".splitlines()

def readf():
    INPUT_FILENAME = '/home/yonch/Downloads/A-small-attempt0.in'
    return file(INPUT_FILENAME).read().splitlines()

if __name__ == '__main__':
    lines = readf()
    l, lines = eat(lines)
    N = int(l)
    outfile = ""
    for i in xrange(N):
        l, lines = eat(lines)
        x = int(l)
        s1 = set(lines[x-1].split(" "))
        lines = lines[4:]
        l, lines = eat(lines)
        x = int(l)
        s2 = set(lines[x-1].split(" "))
        lines = lines[4:]
        s = s1.intersection(s2)
        if len(s) == 0:
            res = "Volunteer cheated!"
        elif len(s) > 1:
            res = "Bad magician!"
        else:
            res = list(s)[0]
        outline = "Case #%d: %s" % (i+1, res)
        print outline
        outfile += outline + "\n"
    
    file('/home/yonch/Downloads/Solution.out','w').write(outfile)