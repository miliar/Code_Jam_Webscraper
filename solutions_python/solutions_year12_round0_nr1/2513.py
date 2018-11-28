#input = open("q1_test.txt", 'r')
input = open("q1.txt", 'r')

c = -1
cases = 0
dic = dict({'y':'a',
'n':'b',
'f':'c',
'i':'d',
'c':'e',
'w':'f',
'l':'g',
'b':'h',
'k':'i',
'u':'j',
'o':'k',
'm':'l',
'x':'m',
's':'n',
'e':'o',
'v':'p',
'z':'q',
'p':'r',
'd':'s',
'r':'t',
'j':'u',
'g':'v',
't':'w',
'h':'x',
'a':'y',
'q':'z'
})
    
for line in input:

    tmp =""
    c += 1
    if c == 0:
        cases = int(line)
        continue
        
    for ch in line:
        if ord(ch) < 123 and ord(ch) > 96:
            tmp += dic[ch]
        else:
            if ch != '\n':
                tmp += ch       
        

    print "Case #"+str(c)+": "+tmp
    #print "\n"