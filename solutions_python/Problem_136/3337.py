'''
Created on Apr 12, 2014

@author: richard
'''


def timeGivenFarms(x, farms, f, c):
  
  time = 0
  for i in range(0, farms):
    time += timeForFarm(c, i, f)\
  
  return (x/(((farms * f) + 2))) + time

def timeForFarm (c, farms,f):
  
  return c/(((farms * f) + 2)) 

if __name__ == '__main__':
  
  import sys
  
  fileName = sys.argv[1]
  lines = open(fileName).readlines()
  nCases = lines[0]
  for case in range(1, int(nCases)+1):
    args = lines[case].split()
    c = float(args[0])
    f = float(args[1])
    x = float(args[2])
    results = []
    best = timeGivenFarms(x, 0, f, c)
    for farms in range(0,9999):
      t = timeGivenFarms(x, farms, f, c)
      results.append((farms, timeGivenFarms(x, farms, f, c)))
      if t <= best: 
        best = t 
      else: 
        break
#     results = [(farms, timeGivenFarms(x, farms, f, c)) for farms in range(0,10)]
    print 'case #%d: %f' %(case, sorted(results, key = lambda tup: tup[1] )[0][1])
#     print results
#     print timeGivenFarms(x, 0, f, c)
    