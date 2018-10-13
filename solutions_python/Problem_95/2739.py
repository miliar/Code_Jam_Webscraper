from string import maketrans
import string

intab = " abcdefghijklmnopqrstuvwxyz"
outtab = " yhesocvxduiglbkrztnwjpfmaq"
trantab = maketrans(intab, outtab)
str2 = []
var = raw_input();
#for x in range (1,int(var)+1):
str1 = raw_input()
#for line in str1:
str2 = string.split(str1,'\n')
for x in range (1,int(var)+1):
    print ("Case #"+str(x)+": "+str2[x-1].translate(trantab))
