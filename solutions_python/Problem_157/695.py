# @author Carlos M. Pascal 
# @email cpascal at ac.tuiasi.ro
# Problem C

dic = {}
## -group I
dic['11']='1'
dic['1i']='i'
dic['1j']='j'
dic['1k']='k'
##
dic[('i1')]='i'
dic[('ii')]='-1'
dic[('ij')]='k'
dic[('ik')]='-j'
##
dic[('j1')]='j'
dic[('ji')]='-k'
dic[('jj')]='-1'
dic[('jk')]='i'
##
dic[('k1')]='k'
dic[('ki')]='j'
dic[('kj')]='-i'
dic[('kk')]='-1'
##
## -group II
dic[('-11')]='-1'
dic[('-1i')]='-i'
dic[('-1j')]='-j'
dic[('-1k')]='-k'
##
dic[('-i1')]='-i'
dic[('-ii')]='1'
dic[('-ij')]='-k'
dic[('-ik')]='j'
##
dic[('-j1')]='-j'
dic[('-ji')]='k'
dic[('-jj')]='1'
dic[('-jk')]='-i'
##
dic[('-k1')]='-k'
dic[('-ki')]='-j'
dic[('-kj')]='i'
dic[('-kk')]='1'

    
def lookup(c, str):
  if str=='':
    yield False, str
  else:
    if str[0]==c:
      yield True, str[1:]
    answer = str[0]
    for x in range(1, len(str)):
      answer = dic[answer+str[x]]
      if answer==c:
        yield True, str[x+1:]
    yield False, ''
    
def eval(str):
  if str=='':
    return ''
  answer = str[0]
  for x in range(1, len(str)):
    answer = dic[answer+str[x]]
  return answer
    
    
def isCorrect(str, x):
  count = 0
  #print str
  for a,aaa in lookup('i',str*x):
    #print 'a:',a, aaa
    if a:
      for b, bbb in lookup('j',aaa):
        count+=1
        #print 'b:',b, bbb
        if b and 'k'==eval(bbb):
          #print 'c: True'
          #print "c:", count
          return True
        if count>1000:
          return False
  #print count
  #print "c:",count
  return False

def isInInterval(x, start, step):
  p = start
  while (p<x+step):
    #print p
    if x==p:
      return True
    p+= step
  return False

def zip(case, xx): 
  ans = []
  for x in range(1,min(xx+1, 30)):
    #print x
    answer = isCorrect(case, x) 
    if answer:
      ans.append(x)
    if len(ans)==2:
      break
  print ans
  if len(ans)==2:
    df = ans[1]-ans[0]
    return isInInterval(xx, ans[0] ,df)
  if ans and ans[0]==xx:
    return True
  return False



case = 'ijjkkkj'
xx = 1146

case = 'i'
xx = 3863
case = 'kiij'
xx = 3
#case = 'ji'
#xx = 6
case = 'ik'
xx = 4214
#case = 'ikiij' #1805 ;not par
#xx = 1805

#case = 'kjjijjjkiiiikjkjkijjikiijijkkiijkikkikiiijkiiiijkkkikkjkjikiijkijkjijijkjkjkjiikikjkkkiikjijkijkjiji' #100
#xx = 100

#case = 'kikkiij' #1323
#xx = 1323
#print zip(case, xx)

#print eval('ijk')

 


  
#answer = isCorrect(case, 100) 
#print "Answer: ",100, answer


def doWork(input, output):
  fin = open(input)
  fout = open(output, 'w')
  no_cases = int(fin.readline())
  no = 0
  while (no_cases>no):
    no+=1
    L, X = fin.readline().split()
    str = fin.readline().split()
    
    print no,L,X, eval(str[0]*int(X))
    
    answer =  zip(str[0], int(X))
    #answer = True
    if answer:
      msg = 'Case #{0}: {1}\n'.format(no, 'YES')
    else:
      msg = 'Case #{0}: {1}\n'.format(no, 'NO')
    print msg
    fout.write(msg)

  fin.close()
  fout.close()

input = 'D:\work\codejam2015\prC\inprC.txt'
output = 'D:\work\codejam2015\prC\outprC.txt'
doWork(input, output)
  
""" 
def main():
  
if __name__ == '__main__':
  main()
"""
    