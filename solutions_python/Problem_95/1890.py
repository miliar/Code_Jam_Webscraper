from string import maketrans   # Required to call maketrans function.


dic = {'a':'y', 'b':'h', 'c':'e', 'd':'s', 'e':'o', 'f':'c', 'g':'v', 'h':'x',
        'i':'d', 'j':'u', 'k':'i', 'l':'g', 'm':'l', 'n':'b', 'o':'k', 'p':'r',
        'q':'z', 'r':'t', 's':'n', 't':'w', 'u':'j', 'v':'p', 'w':'f', 'x':'m',
        'y':'a', 'z':'q'}
        
intab = "acbedgfihkjmlonqpsrutwvyxz"
outtab = "yehosvcdxiulgkbzrntjwfpamq"

trantab = maketrans(intab, outtab)

def translate(s):
    sl = s.splitlines()
    n,sl = int(sl[0]), sl[1:]
    for i in range(n):
        print "Case #" + str(i+1) + ": " + sl[i].translate(trantab)
        

