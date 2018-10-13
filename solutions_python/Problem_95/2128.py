n=int(raw_input())
def decode(s):
  x=''
  for i in range(len(s)):
    if s[i]=='y':
      x+='a'
    elif s[i]=='n':
      x+='b'      
    elif s[i]=='f':
      x+='c'
    elif s[i]=='i':
      x+='d'
    elif s[i]=='c':
      x+='e'
    elif s[i]=='w':
      x+='f'
    elif s[i]=='':
      x+='f'
    elif s[i]=='l':
      x+='g'
    elif s[i]=='b':
      x+='h'
    elif s[i]=='k':
      x+='i'
    elif s[i]=='u':
      x+='j'
    elif s[i]=='o':
      x+='k'
    elif s[i]=='m':
      x+='l'
    elif s[i]=='x':
      x+='m'
    elif s[i]=='s':
      x+='n'
    elif s[i]=='e':
      x+='o'
    elif s[i]=='v':
      x+='p'
    elif s[i]=='p':
      x+='r'
    elif s[i]=='d':
      x+='s'
    elif s[i]=='r':
      x+='t'
    elif s[i]=='j':
      x+='u'
    elif s[i]=='z':
      x+='q'
    elif s[i]=='h':
      x+='x'
    elif s[i]=='a':
      x+='y'
    elif s[i]=='t':
      x+='w'    
    elif s[i]=='g':
      x+='v'
    elif s[i]=='q':
      x+='z'

    
    else:
      x+=s[i]
  return x
    
for i in range(n):
  print 'Case #'+str(i+1)+': '+decode(raw_input())
  
  