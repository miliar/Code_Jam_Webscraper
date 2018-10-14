import sys

def eval_triple(sums, beat_score, strange_no):
  gd = 0
  
  for kk in range(len(sums)):
    k = int(sums[kk])

    if k==0 and beat_score>0:
      continue
    elif int(k/3) >= beat_score:
      gd += 1
      continue
    else:
      num1=int(k/3)
      if (k-num1)%2 == 0 and strange_no>0:
        if ((k-num1)/2+1) >= beat_score:
          gd += 1
          strange_no -= 1
          continue
        else:
          num2 = int((k-num1)/2)
          num3 = k-num1-num2

          if num1 >= beat_score or num2 >= beat_score or num3 >= beat_score:
            gd += 1
      else:
        num2 = int((k-num1)/2)
        num3 = k-num1-num2

        if num1 >= beat_score or num2 >= beat_score or num3 >= beat_score:
          gd += 1

  return gd



res = ""

with open(sys.argv[1], 'r') as fin:

    line = fin.readline()
    linenum = int(line.strip())
 
    for i in range(linenum):
      line = fin.readline()

      resl = 0
      tline = line.split(' ')
      snum = int(tline[1])
      high = int(tline[2])

      resl = eval_triple(tline[3:], high, snum)

      res += "Case #"+str(i+1)+": "+str(resl)+"\n"

with open("out.txt", 'w') as fout:
  fout.write(res)

