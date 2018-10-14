dic={'\t':'\t','\n':'\n',' ':' ','a':'y', 'b':'h','c':'e','d':'s','e':'o','f':'c','g':'v','h':'x','i':'d','j':'u','k':'i','l':'g','m':'l','n':'b','o':'k','p':'r','q':'z','r':'t','s':'n','t':'w','u':'j','v':'p','w':'f','x':'m','y':'a','z':'q'}
f = open("/home/alaa/Desktop/codejam/A-small-attempt0.in")
f.readline()
f.readline()

output = open("/home/alaa/Desktop/codejam/output.txt" , 'w')
cnt = 1
try:
    for line in f:
        tr_sen = ('CASE #%d: ')%(cnt)
        for i in line:
            tr_sen += dic[i]
        
        output.write(tr_sen+'\n') 
        cnt+=1
finally:
    f.close()
    output.close()
    


  
    
