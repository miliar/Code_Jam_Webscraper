from sys import argv

script, filename = argv

mapping=['y','h','e','s','o','c','v','x','d','u','i',
     'g','l','b','k','r','z','t','n','w','j','p','f','m','a','q']

txt = open(filename)
outf = open("output.txt", 'w')

T = int(txt.readline())

for i in range(0,T):
    S = txt.readline()
    temp = list(S)
    for j in range(0, len(S)):
        if ((ord(temp[j])- ord('a')) in range(0,26)):
            temp[j]=mapping[ord(temp[j])-ord('a')]
    S="".join(temp)

    outf.write("Case #")
    outf.write(str(i+1))
    outf.write(": ")
    outf.write(S)

txt.close()
outf.close()
        
        
    
