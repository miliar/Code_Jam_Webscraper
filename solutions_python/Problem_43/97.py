itoa = {0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',
      10:'a',11:'b',12:'c',13:'d',14:'e',15:'f',16:'g',17:'h',18:'i',
      19:'j',20:'k',21:'l',22:'m',23:'n',24:'o',25:'p',26:'q',27:'r',
      28:'s',29:'t',30:'u',31:'v',32:'w',33:'x',34:'y',35:'z'}

f = open('file.txt')
T = int(f.readline())

t = 0
while t != T:
   t += 1

   N = f.readline().strip()
   base = max(len(set(N)),2)
   convert = {}
  
   convert[N[0]] = '1'
   for c in N:
      if c != N[0]:
         convert[c] = '0'
         break

   N = list(N)
   b = 2
   for i in xrange(len(N)):
      if N[i] not in convert:
         convert[N[i]] = itoa[b]
         b += 1
      N[i] = convert[N[i]]

   print "Case #%d: %d" % (t, int(''.join(N), base))

f.close()

