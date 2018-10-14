import string
# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="srpoder"
__date__ ="$03-sep-2009 13:57:46$"

#if __name__ == "__main__":
#    print "Hello World";
#


phrase = "welcome to code jam"
def cauntos(case,text):
  dp = [[0] * (len(phrase)+1) for i in xrange(len(text)+1)]
  for i in xrange(len(text)):
    dp[0][0] = dp[i+1][0] = 1
    for j in xrange(len(phrase)):
      if text[i] == phrase[j]:
        dp[0][j+1] += dp[0][j]
        dp[0][j+1] %= 10000
  ans = sum([row[-1] for row in dp])
  return "Case #%d: %04d" % (case, ans)

#cauntos(1,"welcome to code jam");

f=file("C-large.in")
lines=string.split(f.read(),"\n");


salida="";
for i in range(1,int(lines[0])+1):
    salida+=cauntos(i, lines[i])+"\n"

f2=file("C-large.out","w")
f2.write(salida);


