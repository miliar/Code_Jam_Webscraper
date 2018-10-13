f = open('/home/dexter/input5.in', 'r')

cases = int(f.readline())

def equal(items):
    out =False
    p=items[0]
    if(p=='.'):
        return (False,'.')
    for k in items:
        if k==p or k=='T':
            out=True
        else :
            out =False
            break
    return (out,p)
      
def winner(s):
   win_rows =[[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15],
            [0,4,8,12],[1,5,9,13],[2,6,10,14],[3,7,11,15],
            [0,5,10,15],[3,6,9,12]]
   for rows in win_rows:
        l=equal([s[i] for i in rows])
        if l[0]:
            return l[1]+" won"
   if s.find('.')!=-1:
         return "Game has not completed"
   else:
         return "Draw"
            
            
for i in range (0, cases):
    s=''
    for k in range(0,4):
        xs = f.readline()
        s=s+xs
        s=s.split()
        s=''.join(s)        
    a=f.readline()
    print "Case #"+str(i+1)+": "+winner(s)
