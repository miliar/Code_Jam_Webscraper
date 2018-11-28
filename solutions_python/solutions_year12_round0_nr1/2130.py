def replace_all(text, old, new):
    newtext=''
    for i in range(0,len(text)):
        if text[i]==' ':
            newtext=newtext+' '
        for j in range(0,len(old)):
            if old[j]==text[i]:
                newtext=newtext+new[j]
                break

    return newtext
 
 
 
def translate(text):
        newtext=replace_all(text,'abcdefghijklmnopqrstuvwxyz','yhesocvxduiglbkrztnwjpfmaq')
        return newtext
    
import sys
fin =open("A-small-attempt.in", "r")
N = int(fin.readline())
for case in range(1,N+1):
    text = fin.readline()
    answer=translate(text)
    
    print "Case #%d: %s" % (case, answer)
    
