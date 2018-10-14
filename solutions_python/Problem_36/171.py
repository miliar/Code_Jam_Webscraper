infn="C-large.in"
outfn="laout.txt"

rev=10000

def indexes(c, s):
   res=[]
   for i in range(len(s)):
       if s[i]==c:
           res.append(i)
   return res
   
def set(m, n , p, v):
   while len(m)<=n:
       m.append([])
   while len(m[n])<=p:
       m[n].append(None)
   m[n][p]=v % rev
   
def get(m, n, p):
   if p<0:
       return 0
   if len(m) <= n:
       #new row
       return 0
   if len(m[n])==0:
       #empty row
       return 0;
   #otherwise return last cell in row
   return m[n][len(m[n])-1];

input=open(infn)
out=open(outfn, 'w')
cases = int(input.readline())
s = list("welcome to code jam")
for caseid in range(1, cases+1): 
   line = input.readline()
   if 'w' in list(line):
       line = list(line[line.index('w'):])
       line = filter(lambda x: x in s, line)
       
       #let fill m(n, p) where m(n,p) means how many ways we can put n first pattern chars in starting l chars of line
       # so finally we need m(len(s), len(line))
       #how to get 
       m = []
       m.append([1])
       n = 0
       p = 1
       sn = s[0]
       filled = False;
       while p < len(line):
           for N in indexes(line[p], s):
               if N==0:
                   set(m, N, p, get(m, N, p-1) + 1)
               else:
                   set(m, N, p, get(m, N, p-1) + get(m, N-1, p-1))
           p += 1;
       
       rr = 0
       if len(m)>=len(s):
           rr = m[len(m)-1].pop()
   else: rr = 0
   rr = str(rr);
   while len(rr) < 4:
       rr = "0" + rr;
   out.write("Case #" + str(caseid) + ": " + rr)
   out.write("\n")
   print('.')