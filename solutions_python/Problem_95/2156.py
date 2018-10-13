fin=open('input.txt', 'r')
fout=open('output.txt', 'w')
t='yhesocvxduiglbkrztnwjpfmaq'

def translate(x):
    return t[ord(x)-ord('a')] if x.isalpha() else x

n=int(fin.readline())
for i in range(n):
    s=fin.readline()
    s='Case #'+str(i+1)+': '+''.join(map(translate,s))
    fout.writelines(s)