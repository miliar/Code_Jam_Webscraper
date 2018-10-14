#!/grid/common/pkgs/python/v3.2.2/bin/python3
import sys;

def sol(N, K):
  big = N//2
  small = (N-1)//2

  if K==1:
    return str(big) + ' ' + str(small)
  if K%2==0:
    return sol(big, K//2)
  else:
    return sol(small, K//2)

if __name__ == '__main__':
  if len(sys.argv)<2:
    print(sys.argv[0]+' <file_name>')
    exit()

  with open(sys.argv[1], 'r') as data_file:
    cas = -1
    k = 0

    for line in data_file:
      if cas==-1:
        cas = int(line.strip())
      else:
        lst = line.strip().split(' ')
        total = int(lst[0])
        num = int(lst[1])
        k = k + 1
        print('Case #'+str(k)+': '+sol(total, num))
