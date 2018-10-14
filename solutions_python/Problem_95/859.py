'''
googlereese  = ["ejp mysljylc kd kxveddknmc re jsicpdrysi" , "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd" , "de kr kd eoya kw aej tysr re ujdr lkgc jv"]
english = ["our language is impossible to understand", "there are twenty six factorial possibilities", "so it is okay if you want to just give up"]

# From the initial hint given
translator_from_english = { 'a': 'y', 'o': 'e', 'z': 'q', 'q': 'z'}

# Now build the translator based on the test cases
for case in range(len(googlereese)):
  secret = googlereese[case]
  truth = english[case]
  for pos in range(len(secret)):
    translator[truth[pos]] = secret[pos]

print "{"
for char in 'abcdefghijklmnopqrstuvwxyz':
  print "'",char,"'", ":" , "'",translator[char],"',",
print "}"
'''

translator_from_english =  {'a':'y','b':'n','c':'f','d':'i','e':'c','f':'w','g':'l','h':'b','i':'k','j':'u','k':'o','l':'m','m':'x','n':'s','o':'e','p':'v','q':'z','r':'p','s':'d','t':'r','u':'j','v':'g','w':'t','x':'h','y':'a','z':'q',' ':' '}
translator_to_english = {' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q'}

T = int(raw_input())
for i in range(1,T+1):
  googlereese = raw_input()
  english = ''
  for char in googlereese:
    english += translator_to_english[char]
  print "Case #%d: "%i, english