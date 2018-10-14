import sys

res = ""

with open(sys.argv[1], 'r') as fin:

    line = fin.readline()
    linenum = int(line.strip())

    j=0
    for i in range(linenum):
      line = fin.readline()
      resl = 0
      
      pair = line.strip().split(' ')
      aint = int(pair[0])
      bint = int(pair[1])
      last = [0,0]
      
      for k in range(aint, bint+1):
        kstr = str(k)
        kval = []
        for i in range(len(kstr)):
          ktmp = int(kstr[len(kstr)-i:] + kstr[0:len(kstr)-i])
          if ktmp != k and aint<=ktmp and ktmp<=bint and k<ktmp and last != [k, ktmp]:
            resl += 1
            last[0] = k
            last[1] = ktmp

      j += 1
      res += "Case #"+str(j)+": "+str(resl)+"\n"

with open("out.txt", 'w') as fout:
  fout.write(res)
      

          
