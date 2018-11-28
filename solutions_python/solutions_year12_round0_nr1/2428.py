l = open("input.txt", "r").readlines()
fo = open("output.txt", "w")
cs = 0
d = {'a':'y', 'c':'e', 'b':'h', 'e':'o', 'd':'s', 'g':'v', 'f':'c', 'i':'d', 'h':'x', 'k':'i', 'j':'u', 'm':'l', 'l':'g', 'o':'k', 'n':'b', 'p':'r', 's':'n', 'r':'t', 'u':'j', 't':'w', 'w':'f', 'v':'p', 'y':'a', 'x':'m', 'z':'q', 'q':'z', ' ':' ', '\n':''}
for i in l[1:]:
    cs += 1
    s = ''
    fo.write("Case #" + str(cs) + ": ");
    for j in range(len(i)):
        s += d[i[j]]
    fo.write(s + "\n")