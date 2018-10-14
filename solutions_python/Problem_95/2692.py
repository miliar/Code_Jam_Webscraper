# Author: Bhanu Chandar

f = open('A-small-attempt4.in','r')  # File Realding and writing
fout = open("output.txt", "w") 

q="abcdefghijklmnopqrstuvwxyz"  # String comparition
k="yhesocvxduiglbkrztnwjpfmaq"

n=1

for line in f.readlines():
        if n>1:
                n1=""
                n1=n1+"Case #"+(str)(n-1)+": "
                print "\n",
                
                for j in range(len(line)):
                        if line[j] in q:
                                a=(int)(q.index(line[j]))
                               # print k[a],
                                n1=n1+k[a]
                        else:
                                #print line[j],
                                n1=n1+line[j]
                #print n1
                fout.write(n1)
                #fout.write("\n")
        n=n+1
	
f.close()
fout.close()



