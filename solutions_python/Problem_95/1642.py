dictionary = {'a':'y',
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
              ' ':' ',
              '\n':'\n'}
              
              

cypherin	=	open("A-small-attempt1.in","r")
f=open("A-small-attempt1.out","w")
count=cypherin.readline();
k=1
for cyp in cypherin:
        f.write("Case #"+repr(k)+": ");
        for i in range(0,len(cyp)):
            f.write(dictionary[cyp[i]]);
        k+=1
f.close();
