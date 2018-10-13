import sys

def switch(n):
   return {'y':'a','n':'b','f':'c','i':'d','c':'e','w':'f','l':'g','b':'h','k':'i','u':'j','o':'k','m':'l','x':'m','s':'n','e':'o','v':'p','z':'q','p':'r','d':'s','r':'t','j':'u','g':'v','t':'w','h':'x','a':'y','q':'z',' ':' '}[n]
   
Translation=[]
sys.stdin = open('A-small-attempt0.in')
Output = open('output.txt','w+')

T=input()

for i in range(T):
   IN=raw_input()
   Sentence=""
   for letter in IN:
      Sentence+=switch(letter)
   Translation.append(Sentence)
for i in range(T):
   Output.write ("Case #%d: "%(i+1)+Translation[i]+"\n")

#print "File writing Done;"
Output.close()


