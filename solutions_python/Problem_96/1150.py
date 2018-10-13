# programing language python3
# problem: Dancing With the Googlers

def topScore(x):
  ns = 0                      #non surprising highest score
  s = 0                       #surprising highest score
 
  n = x % 3
  if n == 2:
    ns = (x +1)//3
    s = (x -2 )//3 + 2
  elif n == 1:
    ns = (x -1)//3 +1
    s = (x - 4) //3 +2
  else:
    ns = x // 3
    s = (x -3)//3 +2
  if (x<=1):
    s = 0
  if (x>=29):
    s = 10
  return (ns, s)
def find(S,p,new_list):
  new_list = sorted(new_list,key = lambda new: new[0])
  count = 0;
  for each in new_list:
    if (p<= each[0]):
      count+=1
    elif(p<=each[1] and S>0):
      count +=1
      S-=1
  return count


def main():
  file_input = open('input.txt')        # reading input from this file
  file_output = open('output.txt', 'w') # this is the output file
  T = file_input.readline()
  T = int(T[:-1])
  for x in range(1, T+1):
    _S = file_input.readline()
    _S = _S.split()
    li = []
    for each in _S:
      li.append(int(each))
    N = li[0]
    S = li[1]
    p = li[2]
    li = li [3:]
    new_list = []
    for each in li:
      new_list.append(topScore(each))
    y = find(S,p,new_list)
    file_output.write('Case #'+str(x)+": "+str(y)+'\n')


if __name__ == '__main__':
  main()
