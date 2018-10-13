import pickle
trans = {'a':'y','b':'h','c':'e','d':'s','e':'o','f':'c','g':'v','h':'x','i':'d','j':'u','k':'i','l':'g','m':'l','n':'b','o':'k','p':'r','q':'z','r':'t','s':'n','t':'w','u':'j','v':'p','w':'f','x':'m','y':'a','z':'q'}

def translator(G):
    sen_trans = ''
    words = G.split()
    for word in words:
        for letter in word:
            letter = trans[letter]
            sen_trans += letter
        sen_trans += ' '
    return sen_trans

def io(inp):
    x = open(inp, 'r').read()
    x = x.split('\n')
    T = x[0]
    count = 0
    result = open('result.txt','a')
    for G in x[1:]:
        count += 1
        if count <= 30:
            y = translator(G)
            result.write('Case #' + str(count) + ': ' + y + '\n')
    result.close()
    
inp = input('Insert file url: ')
io(inp)
