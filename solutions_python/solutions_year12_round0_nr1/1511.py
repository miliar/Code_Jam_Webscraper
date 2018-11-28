fout=open('C:\\Users\Tahsin\Desktop\CodejamCode\outA.txt','w')
fin=open('C:\\Users\Tahsin\Downloads\A-small-attempt0.in','r')
tests=int(fin.readline().strip())

#tests=int(input())

lettermap={' ':' ','a':'y','b':'h','c':'e','d':'s','e':'o','f':'c','g':'v','h':'x','i':'d','j':'u','k':'i','l':'g','m':'l','n':'b','o':'k','p':'r','q':'z','r':'t','s':'n','t':'w','u':'j','v':'p','w':'f','x':'m','y':'a','z':'q'}
for test in range(tests):
    
    line=fin.readline().strip()
    
    fout.write("Case #{0}: ".format(test+1))
    for letter in line:
        fout.write(lettermap[letter])
    fout.write('\n')
    
        
    
    
    