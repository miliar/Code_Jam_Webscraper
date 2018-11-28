import sys

t = int(sys.stdin.readline())
fa_row = ''
sa_row = ''
a = []
b = []
aset = {}
bset = {}
output = ''

for tc in range(0,t):
    fa = int(sys.stdin.readline())
    for i in range(0,4):
        if(i == (fa - 1)) : 
            fa_row = sys.stdin.readline()
        else:
            sys.stdin.readline()

    sa = int(sys.stdin.readline())
    for i in range(0, 4):
        if(i == (sa - 1)):
            sa_row = sys.stdin.readline()
        else:
            sys.stdin.readline()    

    a = list(fa_row.split(' '))
    b = list(sa_row.split(' '))
    a[-1] = a[-1].strip()
    b[-1] = b[-1].strip()

    aset = set(a)
    bset = set(b)
    res = aset.intersection(bset)
    if not res:
      output += "Case #"+str(tc+1)+": Volunteer cheated!" + '\n'
    else:
      if len(res) == 1:
        output += "Case #"+str(tc+1)+": "+list(res)[0]+ '\n'
      else:
        output +="Case #"+str(tc+1)+": Bad magician!\n"
else:
  print(output.strip())
    
