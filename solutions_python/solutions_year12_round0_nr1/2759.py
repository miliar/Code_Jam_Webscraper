from string import maketrans

outtab =  "yhesocvxduiglbkrztnwjpfmaq"
intab = "abcdefghijklmnopqrstuvwxyz"
trantab = maketrans(intab, outtab)

f = open("/home/kyaordean/Dropbox/CodeJam/A-small-attempt6.in", "r")
g = open("/home/kyaordean/Dropbox/CodeJam/output6.txt", "w")
c = range(int(f.readline()))

for i in c :
      linea = f.readline()
      g.write('Case #'+ str(i+1) + ': '+linea.translate(trantab))   

f.close()
g.close()
