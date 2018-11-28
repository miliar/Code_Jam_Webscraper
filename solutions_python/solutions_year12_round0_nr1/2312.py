#bicorn: Python27

def Translate(googlerese):
    a = tuple(googlerese)
    trans_dict = {'a':'y','b':'h','c':'e','d':'s','e':'o','f':'c','g':'v','h':'x','i':'d',
                  'j':'u','k':'i','l':'g','m':'l','n':'b','o':'k','p':'r','q':'z','r':'t',
                  's':'n','t':'w','u':'j','v':'p','w':'f','x':'m','y':'a','z':'q',' ':' '}
    s = ''
  
    for elem in a:
        if trans_dict.has_key(elem):
            s += trans_dict[elem]
    s += '\n' 
    return s
   
    
if __name__ == "__main__":
    f = open(r'./A-small-attempt1.in')
    outfile = open('a.txt', 'a')
    T = int(f.readline())
    for glerese in range(1,T+1):
        outfile.write("Case #%d: %s" % (glerese,Translate(f.readline())))