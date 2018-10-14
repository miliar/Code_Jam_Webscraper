def function(x, j):
    y = len(x)
    a=[]
    i = 0
    while(i< y):
        if(x[i] == ' '):
            a.append(" ")
        else: a.append(d[x[i]])
        i = i + 1
    s = ''.join(a)
    fw.write("Case #" + str(j) + ": " + s+'\n')

d = {'a':'y',
     'b':'h',
     'c':'e',
     'd':'s',
     'e':'o',
     'f':'c',
     'g':'v',
     'h':'x',
     'i':'d',
     'j':'u',
     'k':'i',
     'l':'g',
     'm':'l',
     'n':'b',
     'o':'k',
     'p':'r',
     'q':'z',
     'r':'t',
     's':'n',
     't':'w',
     'u':'j',
     'v':'p',
     'w':'f',
     'x':'m',
     'y':'a',
     'z':'q',
     '\n': '',
    }


j = 0
fr = open("test.txt" , 'r')
fw = open("output.txt", 'w')

for line in fr:
    x = line
    if j>0:
        function(x, j)    
    j= j + 1
fr.close()
fw.close()