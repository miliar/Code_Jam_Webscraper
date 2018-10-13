from pqdict import pqdict

file_in = open('C-large.in')
file_out = open('C-large.out', 'w')

T = int(file_in.readline())

def big_n_small(number):
  number -= 1
  half = number // 2
  return (number - half, half)

for t in range(1, T+1):
  count = 0
  N, K = map(int, file_in.readline().split())
  slots = pqdict({ N: (N, 1)}, reverse=True)
  last = -1
  while K > 0:
    last, count = slots.popitem()[1]
    # print(K)
    # print(last, count)
    # break
    K -= count
    big, small = big_n_small(last)
    if big not in slots: slots[big] = (big, 0)
    if small not in slots: slots[small] = (small, 0)
    slots[big] = (big, slots[big][1]+count)
    slots[small] = (small, slots[small][1]+count)
    # print(slots)
    # break
  # print(last)
  big, small = big_n_small(last)
  file_out.write('Case #' + str(t) + ': ' + str(big) + ' ' + str(small) + '\n')
