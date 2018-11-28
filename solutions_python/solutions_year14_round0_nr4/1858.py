f=open("D-small-attempt0.in","r")
out = open('out', 'w')
T=int(f.readline())

for i in range(T):
  N=int(f.readline())
  row=map(float,str(f.readline()).split())
  sorted_naomi=sorted(row, key=float)
  row=map(float,str(f.readline()).split())
  sorted_ken=sorted(row, key=float)
  naomi_wins_opt=0
  naomi_wins_deceit=0
  #optimal
  for x in range(N):
    chosen=sorted_naomi[x]
    for block in sorted_ken:
      if block>chosen:
        sorted_ken.remove(block)
        break
    if block<chosen:
      sorted_ken.remove(sorted_ken[0])
      naomi_wins_opt+=1
  #deceitful
  sorted_ken=sorted(row, key=float)
  for x in range(N):
    target=sorted_ken[-x-1]
    for block in sorted_naomi:
      if block>target:
        sorted_naomi.remove(block)
        naomi_wins_deceit+=1
        break      
    if block<target:
      deceitful_block=target-.0000001
      sorted_naomi.remove(sorted_naomi[0])
  out.write("Case #"+str(i+1)+": "+str(naomi_wins_deceit)+" "+str(naomi_wins_opt)+"\n")



