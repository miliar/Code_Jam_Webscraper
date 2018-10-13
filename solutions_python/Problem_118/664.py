import sys
from math import log, floor, ceil

def rev_num(i):
  return int(str(i)[::-1])

def gen_pali(start, end):
  for i in xrange(start, min(10, end)):
    yield i

  len_end = int(ceil(log(end+1, 10)))
  len_start = int(ceil(log(start+1, 10)))

  half_end = int(10 ** (ceil(len_end / 2.))) - 1
  half_start = int(10 ** ((floor(len_start / 2.))))

  stopa = False
  stopb = False
  r10 = range(10)
  
  for i in xrange(1, half_end):
    if stopa:
      break
    curr_len = int(ceil(log(i+1, 10)))
    mult = 10 ** curr_len
    rev = rev_num(i)
    num = (i * mult + rev)
    if num > end:
      stopa = True
    if start <= num <= end:
      yield num
    if stopb:
      continue
    base_num = (i * mult * 10 + rev) 
    for mid in r10:
      num = base_num + mid * mult 
      if num > end:
        stopb = True
        break
      if start <= num <= end:
        yield num

def input(filename):
  f = open(filename)
  num = int(f.readline().strip())
  for i in xrange(num):
    start, end = (int(s) for s in f.readline().strip().split(' '))
    yield start, end 


def is_pali(num):
  return num == rev_num(num)


def do_work(start, end):
  sqrt_start = int(ceil(start ** 0.5))
  sqrt_end = int(floor(end ** 0.5))
  count = 0
  for num in gen_pali(sqrt_start, sqrt_end + 1):
    if is_pali(num ** 2) and start <= num ** 2 <= end:
      count += 1
      #print num, num ** 2, ', ',
  #print
  return count

def do_work2(start, end):
  count = 0
  for i in range(int(start ** 0.5) - 1, int(end ** 0.5) + 1):
    if is_pali(i) and is_pali(int(i ** 2)) and start <= i ** 2 <= end:
   #   print i, i ** 2, ', ',
      count += 1
  #print
  return count


if __name__ == '__main__':
  gen = input(sys.argv[1])
  for i, (start, end) in enumerate(gen):
    print 'Case #%s: %s' % (i+1, do_work(start, end))
    #print 'Case #%s: %s' % (i+1, do_work2(start, end))
