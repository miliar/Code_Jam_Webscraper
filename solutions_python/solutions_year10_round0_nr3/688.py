#!/usr/bin/python -tt

# R is how many times the rollercoaster runs
# k is how many people it can hold total
# groups is the queue
def doWork(R, k, groups):
  totalMoney = 0
  for i in range(R):
    currentTotal = 0
    riding = []
    while True:
      if not groups: 
        break
      if currentTotal+groups[0] <= k: 
        currentTotal += groups[0]
        riding.append(groups.pop(0))
      else: 
        break
    totalMoney += currentTotal
    groups.extend(riding)
  return totalMoney

def main():
  f = open("input", 'rU')
  cases = f.readline()
  print int(cases)
  #doWork(4, 47)
  #return
  
  output = open('output', 'w')
  for i in range(int(cases)):
    line = f.readline().split(" ")
    R = int(line[0])
    k = int(line[1])
    N = int(line[2]) # meh
    line = f.readline().split(" ")
    groups = [int(n) for n in line]
    output.write('Case #'+str(i+1)+': '+ str(doWork(R, k, groups)) +"\n")
    #break
  f.close()
  
if __name__ == '__main__':
  main()
