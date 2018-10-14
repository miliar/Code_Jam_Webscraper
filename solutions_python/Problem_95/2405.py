def decode(confused,event):

    ref = {'y':'a', 'n':'b', 'f':'c', 'i':'d', 'c':'e', 'w':'f', 'l':'g', 'b':'h', 'k':'i', 'u':'j', 'o':'k', 'm':'l', 'x':'m', 's':'n', 'e':'o', 'v':'p', 'z':'q', 'p':'r', 'd':'s', 'r':'t', 'j':'u', 'g':'v', 't':'w', 'h':'x', 'a':'y', 'q':'z', ' ':' ', '\n':'\n'}
    #enter = 'de kr kd eoya kw aej tysr re ujdr lkgc jv'
    ordered = 'Case #' + str(event) + ': '
    
    for letter in confused:
        ordered += ref[letter]
        
    return ordered

data = open('input.in','r')
data = data.readlines()
data = data[1:] #To remove first line

out = open('output.out','w')
event = 1
new_data = []
for item in data:
    out.write(decode(item,event))
    event += 1
    
out.close()

    
                    