g ={'a':'y', 'b':'h', 'c':'e', 'd':'s', 'e':'o', 'f':'c', 'g':'v', 'h':'x', 'i':'d', 'j':'u', 'k':'i', 'l':'g', 'm':'l', 'n':'b', 
'o':'k', 'p':'r', 'q':'z', 'r':'t', 's':'n', 't':'w', 'u':'j', 'v':'p', 'w':'f', 'x':'m', 'y':'a', 'z':'q', ' ':' '} 

file = open('in.txt')
T=int(file.readline())
for i in range(T):
  G=file.readline()
  print 'Case #'+str(i+1)+': '+''.join([g[i] for i in G.rstrip()])
      
