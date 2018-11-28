import os

input=open("input.txt","r")
r=input.readline()

n=r
n=int(n)+1
print n

r=input.readline()
K=1

R=open("output.txt","w")
R.close()

while K < n :
    S=""
    for i in range(0,len(r)-1):
		if r[i]==" ":
			S=S+" "
		elif r[i]=="a":
			S=S+"y"
		elif r[i]=="b":
			S=S+"h"
		elif r[i]=="c":
			S=S+"e"
		elif r[i]=="d":
			S=S+"s"
		elif r[i]=="e":
			S=S+"o"
		elif r[i]=="f":
			S=S+"c"
		elif r[i]=="g":
			S=S+"v"
		elif r[i]=="h":
			S=S+"x"
		elif r[i]=="i":
			S=S+"d"
		elif r[i]=="j":
			S=S+"u"
		elif r[i]=="k":
			S=S+"i"
		elif r[i]=="l":
			S=S+"g"
		elif r[i]=="m":
			S=S+"l"
		elif r[i]=="n":
			S=S+"b"
		elif r[i]=="o":
			S=S+"k"
		elif r[i]=="p":
			S=S+"r"
		elif r[i]=="q":
			S=S+"z"
		elif r[i]=="r":
			S=S+"t"
		elif r[i]=="s":
			S=S+"n"
		elif r[i]=="t":
			S=S+"w"
		elif r[i]=="u":
			S=S+"j"
		elif r[i]=="v":
			S=S+"p"
		elif r[i]=="w":
			S=S+"f"
		elif r[i]=="x":
			S=S+"m"
		elif r[i]=="y":
			S=S+"a"
		elif r[i]=="z":
			S=S+"q"
    R=open("output.txt","a")
    R.write("Case #")
    R.write(str(K))
    R.write(": " + S + "\n")
    R.close()
    r=input.readline()
    K=K+1
    
    
R.close()

