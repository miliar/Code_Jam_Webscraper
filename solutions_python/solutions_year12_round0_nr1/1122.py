def googlrese():
    rev=''
    dic={ 'a':'y','b':'h','c':'e','d':'s','e':'o','f':'c','g':'v','h':'x','i':'d',
          'j':'u','k':'i','l':'g','m':'l','n':'b','o':'k','p':'r','q':'z','r':'t',
          's':'n','t':'w','u':'j','v':'p','w':'f','x':'m','y':'a','z':'q',' ':' ','\n':'\n','.':'.' }
    fil=open('A-small-attempt1.in','r')
    x=fil.readline()
    i=0
    p = open("rever2.in","w")
    while i<int(x):
        rev=''
        y=fil.readline()
        for e in y:
            rev=rev+dic[e]
        p.write("Case #"+str(i+1)+": "+rev)
        i=i+1

    p.close()
    fil.close()

googlrese()
            
            
        
    
