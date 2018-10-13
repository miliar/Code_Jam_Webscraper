#!/usr/bin/python -tt
import sys

opp = {}
comb = {}
#def combine(a,b):
#  if(a in comb):
#    for i in comb[a]:
#      if(i[0] == b):
#        return  i[1]
#  if b in comb:
#    for i in comb[b]:
#      if(i[0] == a):
#        return i[1]
#  return 'XXX'

def combine(ans, e):
#  print ans, "ddD"
  ans.append(e)
  while(len(ans) > 1):
 #   print len(ans)
    done = 0
    if ans[-1] in comb:

      for j in comb[ans[-1]]:
#        print "here"
        if (j[0] == ans[-2]):
          done = 1
          ans[-2] = j[1]
          del(ans[-1])
          break
    if (len(ans)>1 and ans[-2] in comb) and (done == 0):
#       print "hre2"
       for j in comb[ans[-2]]:
        if j[0] == ans[-1]:
          done = 1 
          ans[-1] = j[1]
          del(ans[-2])
          break
#    print ans
    if (done == 0):
      break
 # print "noe, ", ans
  return ans
       

def check_and_clear(ans):
  for i in ans:
    if i in opp:
      for j in opp[i]:
        if j in ans:
          ans = []
          return ans
  return ans

def main():
  t = raw_input()
  t = int(t)
  tp = 0
  while (t>0):
    tp += 1
    t -= 1
    comb.clear()
    opp.clear()


    inp = raw_input()
    inp = inp.split()
    ptr = 0
    i=int(inp[0])
    while(i > 0):
      ptr += 1
      if (inp[ptr][0] not in comb):
        comb[inp[ptr][0]] = [(inp[ptr][1],inp[ptr][2])]
      else:
        comb[inp[ptr][0]].append((inp[ptr][1],inp[ptr][2]))
      i -= 1
    ptr += 1
    i = int(inp[ptr])
    while(i > 0):
      ptr += 1
      if (inp[ptr][0] not in opp):
        opp[inp[ptr][0]] = [inp[ptr][1]]
      else:
        opp[inp[ptr][0]].append(inp[ptr][1])
      i -= 1

    res = inp[-1]
    ans = []
    for i in res:
      ans = combine(ans,i)
 #     print "done 1"
      ans = check_and_clear(ans)
        
        
      #temp = combine(res[i], res[i-1]
      #if(temp != 'XXX'):
      #  res[i-1] = temp
      #  del(res[i])
      #temp = kill(res, i)
      #if(temp != 'XXX'):
    j = 0
    print 'Case #' + str(tp) + ': ',
    sys.stdout.write('[')
    for i in ans:
      j += 1
      sys.stdout.write(i)
      if j != len(ans):
        sys.stdout.write(', ')
    sys.stdout.write(']\n')
      
                    
      
if __name__ == '__main__':
  main()
