f = open("A-small-attempt0.in")

T = int(f.readline())

map = {"y": 'a', 'b':'h', 'c':'e', 'd':'s', 'e':'o', 'f':'c', 'g':'v', 'h':'x', 'i':'d', 'j':'u', 'k':'i', 'l':'g', 'm':'l', 'n':'b', 'o':'k', 'p':'r', 'q':'z', 'r':'t', 's':'n', 't':'w', 'u':'j', 'v':'p', 'w':'f', 'x':'m', 'a':'y', 'z':'q', ' ':' '}

out = open("A-small.out", 'w')

for i in range(T):
    out.write("Case #" + str(i+1) + ": ")
    line = f.readline().strip()
    for c in line:
        out.write(map[c])
    out.write('\n') 

out.close()
f.close()