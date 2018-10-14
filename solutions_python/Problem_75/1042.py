import sys
import time

fin = sys.stdin
fout = open('magicka.out','w')
T = int(fin.readline())
for case in range(1,T+1):
  inp = str(fin.readline()).split()
  numcomb = int(inp[0])
  if numcomb > 0:
    comba = []
    combb = []
    for i in inp[1:numcomb+1]:
      comba.append(i[0:2])
      combb.append(i[2])
  numop = int(inp[numcomb+1])
  if numop > 0:
    op = inp[numcomb+2:numcomb+numop+2] 
  elements = list(inp[numcomb+numop+3])
  spell = []
  for i in elements:
    if len(spell)== 0:
      spell.append(i)
    else:
      if numcomb > 0:
        if spell[-1]+i in comba:
          spell[-1] = combb[comba.index(spell[-1]+i)]
        elif i+spell[-1] in comba:
          spell[-1] = combb[comba.index(i+spell[-1])]
        else:
          spell.append(i)
      else:
        spell.append(i)
      if numop > 0 and len(spell) > 1:
        for j in op:
          j=[j[0],j[1]]
          if spell[-1] in j:
            j.remove(spell[-1])
            for k in spell[:-1]:
              if k in j:
                spell = []
  fout.write("Case #{0}: {1}\n".format(case,str(spell).replace("'","")))
fout.close


