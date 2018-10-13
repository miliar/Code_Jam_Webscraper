dic = {}
dic[1] = [[1,0]]
dic[2] = [[2,0]]
dic[3] = [[3,0]]
dic[4] = [[4,0],[2,1]]
dic[5] = [[5,0],[3,1]]
dic[6] = [[6,0],[3,1]]
dic[7] = [[7,0],[4,1]]
dic[8] = [[8,0],[4,1]]
dic[9] = [[9,0],[5,1],[3,2]]

def evaluate(st): # st = [[1,0], [4,1], [3,2]]
  m1 = 0
  m2 = 0
  for i in range(len(st)):
    if st[i][0] > m1:
      m1 = st[i][0]
    m2 = m2 + st[i][1]
  return m1 + m2

def findmin(l, lst):
  mint = 999999
  pos = [dic[int(lst[i])] for i in range(l)]

  if l == 6:
    for a in pos[0]:
      for b in pos[1]:
        for c in pos[2]:
          for d in pos[3]:
            for e in pos[4]:
              for f in pos[5]:
                k = evaluate([a,b,c,d,e,f])
                if k < mint:
                  mint = k
  if l == 5:
    for a in pos[0]:
      for b in pos[1]:
        for c in pos[2]:
          for d in pos[3]:
            for e in pos[4]:
              k = evaluate([a,b,c,d,e])
              if k < mint:
                mint = k

  if l == 4:
    for a in pos[0]:
      for b in pos[1]:
        for c in pos[2]:
          for d in pos[3]:
            k = evaluate([a,b,c,d])
            if k < mint:
              mint = k

  if l == 3:
    for a in pos[0]:
      for b in pos[1]:
        for c in pos[2]:
          k = evaluate([a,b,c])
          if k < mint:
            mint = k

  if l == 2:
    for a in pos[0]:
      for b in pos[1]:
        k = evaluate([a,b])
        if k < mint:
          mint = k

  if l == 1:
    for a in pos[0]:
      k = evaluate([a])
      if k < mint:
        mint = k

  return mint

# main

infile = open("B-small-attempt0.in", 'r')
outfile = open("B-small.out", 'w')
lines = infile.readlines()
T = int(lines[0])
for i in range(T):
  l = int(lines[2*i+1])
  lst = lines[2*i+2].split(" ")
  outfile.write("Case #{0}: {1}".format(i+1, findmin(l, lst)))
  outfile.write("\n")

outfile.close()
infile.close()
  
