cipher = {' ':' ','y':'a','h':'x','e':'o','s':'n','o':'k','c':'e','v':'p','x':'m','d':'s','u':'j','i':'d','g':'v','l':'g','b':'h','k':'i','r':'t','z':'q','t':'w','n':'b','w':'f','j':'u','p':'r','f':'c','m':'l','a':'y','q':'z'}
read = open('A-small-attempt0.in','r')
wr = open('answer.txt','w')
a = []
c = []
cnt = 0

for line in read:
    a = list(line.strip())
    for x in a: 
        c.append(cipher[x])
    cnt+=1
    c.append('\n')
    wr.write("Case #"+str(cnt)+": "+''.join(c))
    c=[]
    
read.close()
wr.close()
