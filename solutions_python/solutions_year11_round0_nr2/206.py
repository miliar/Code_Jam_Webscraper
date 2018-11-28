from repr import repr

def decrement(cha,chaSet):
  if cha in chaSet:
    chaSet[cha]-=1
    if chaSet[cha]==0:
      chaSet.pop(cha)
    
input  = open('../input/Q_2011_b.in')
CASES  = int(input.readline())
for case in range(CASES):
  args = input.readline().rstrip().split(' ')
  C = int(args[0])
  comb={}
  for i in range(1,C+1):
    pair = args[i][:2]
    el = args[i][2]
    comb[pair]=el
    comb[pair[::-1]]=el
  base=C+1
  opps = {}
  D = int(args[base])
  for i in range(base+1,base+D+1):
    pair = args[i]
    if pair[0] in opps:
      opps[pair[0]].append(pair[1])
    else:
      opps[pair[0]]=[pair[1]]
    if pair[1] in opps:
      opps[pair[1]].append(pair[0])
    else:
      opps[pair[1]]=[pair[0]]
  base=base+D+1
  testString = args[base+1]
  
  resStr=''
  chSet={}
  for ch in testString:
    resStr+=ch
    if ch in chSet:
      chSet[ch]+=1
    else:
      chSet[ch]=1
    pair = resStr[-2:]
    if pair in comb:
      resStr =resStr[:-2]+comb[pair]
      decrement(pair[0], chSet)
      decrement(ch, chSet)
    elif ch in opps:
      list = opps[ch]
      for el in list:
        if el in chSet:
          chSet={}
          resStr=''
          break
  resList = str([a for a in resStr]).replace("'", "")
  print 'Case #'+str(case+1)+': '+resList
  