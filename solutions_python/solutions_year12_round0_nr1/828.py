import sys
import os

if __name__ == "__main__":
  f = open(sys.argv[1])
  fw = open(sys.argv[1]+".answer",'w')
  numlines = int(f.readline())
  
  gtoeng ={'a':'y','b':'h','c':'e','d':'s','e':'o','f':'c','g':'v','h':'x','i':'d','j':'u','k':'i','l':'g','m':'l','n':'b','o':'k','p':'r','q':'z','r':'t','s':'n','t':'w','u':'j','v':'p','w':'f','x':'m','y':'a','z':'q'}
  
  linenum = 1 
  for line in f:
    fw.write("Case #"+str(linenum)+": ")
    linenum+=1
    for c in line:
      if c == ' ':
        fw.write(' ')
      elif c == '\n':
        fw.write('\n')
        continue
      else:
        fw.write(gtoeng[c])

  f.close()
  fw.close()

