d={'a':'y','c':'e','b':'h','e':'o','d':'s','g':'v','f':'c','i':'d','h':'x','k':'i','j':'u','m':'l','l':'g','o':'k','n':'b','p':'r','s':'n','r':'t','u':'j','t':'w','w':'f','v':'p','y':'a','x':'m','q':'z','z':'q'}

output = ''

T = int(raw_input())
for i in range(T):
  G = raw_input()
  S = map(lambda c:' ' if c== ' ' else d[c],G)
  output+='Case #'+str(i+1)+': '+''.join(S)+'\n'

print output
