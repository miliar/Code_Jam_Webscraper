dic = {'a':'y', 'b':'h', 'c':'e', 'd':'s', 'e':'o', 'f':'c', 'g':'v', 'h':'x', 'i':'d', 'j':'u', 'k':'i', 'l':'g', 'm':'l', 'n':'b', 'o':'k', 'p':'r', 'q':'z', 'r':'t', 's':'n', 't':'w', 'u':'j', 'v':'p', 'w':'f', 'x':'m', 'y':'a', 'z':'q', ' ':' '}

f = open('input.in', 'r')
o = open('output.out', 'w')

temp = []
for i in f :
    temp.append(i.rstrip('\n'))
f.close()

n = int(temp[0])

i = 1

for i in range(1, n+1) :
    temp2 = ''
    for x in temp[i] :
        temp2 = temp2 + dic[x]
    o.write('Case #'+ str(i) + ': ' + temp2 + '\n')
    i = i+1
o.close()
