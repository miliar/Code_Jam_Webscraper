f=open('C:/Users/acer/Desktop/CJ/A/A-small-attempt1.txt')
bl=f.readlines()
f.close()
n=bl[0]
k=int(n)
b1='abcdefghijklmnopqrstuvwxyz'
b2='yhesocvxduiglbkrztnwjpfmaq'
from string import maketrans
transcode=maketrans(b1,b2)
f=open('C:/Users/acer/Desktop/CJ/A/sout.txt','w')
i=1
while i <= k :
	f.write('Case #'+ str(i) + ': '+(bl[i].translate(transcode)))
	i=i+1
f.close()
