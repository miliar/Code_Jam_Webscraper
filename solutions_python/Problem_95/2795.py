inp = open(r'e:\downloads\A-small-attempt0.in', 'r')
#inp = open(r'e:\downloads\py.txt', 'r')
#outp = open(r'e:\downloads\py.txt', 'w')
f=inp.readlines()
i=1
lis=[['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'],
      ['y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q','Y','H','E','S','O','C','V','X','D','U','I','G','L','B','K','R','Z','T','N','W','J','P','F','M','A','Q']]
for line in f[1:len(f)]:
    st=''
    for ch in line:
        if ch in lis[0]:
            st+=lis[1][lis[0].index(ch)]
        elif ch=='\n':
            ch='\n'
        else:
            st+=ch
    print 'Case #'+str(i)+': '+st
    i+=1
