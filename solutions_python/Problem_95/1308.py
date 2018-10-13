import sys
f = open('/home/michael/Dropbox/Code Jam/2012/Tongues/In.in')
numcases = int(f.readline())

diction = {'a':'y', 'b':'h', 'c':'e', 'd':'s','e':'o',
              'f':'c','g':'v','h':'x','i':'d','j':'u',
              'k':'i','l':'g','m':'l','n':'b','o':'k',
              'p':'r','q':'z','r':'t','s':'n','t':'w',
              'u':'j','v':'p','w':'f','x':'m','y':'a','z':'q', ' ':' '}
for a in range(numcases):
    print "Case #%d: " % (a+1),
    for character in f.readline():
        if character == "\n":
            print ""
        else:
            sys.stdout.write(diction[character])
