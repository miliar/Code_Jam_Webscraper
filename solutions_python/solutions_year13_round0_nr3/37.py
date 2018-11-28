def check(i):
  if (''.join(reversed(str(i))) != str(i)):
    return None
  a = i * i
  s = str(a)
  if (''.join(reversed(s)) == s):
    return (i, a)
  return None



a = [(0, 0),
 (1, 1),
 (2, 4),
 (3, 9),
 (11, 121),
 (22, 484),
 (101, 10201),
 (111, 12321),
 (121, 14641),
 (202, 40804),
 (212, 44944),
 (1001, 1002001),
 (1111, 1234321),
 (2002, 4008004),
 (10001, 100020001),
 (10101, 102030201),
 (10201, 104060401),
 (11011, 121242121),
 (11111, 123454321),
 (11211, 125686521),
 (20002, 400080004),
 (20102, 404090404),
 (100001, 10000200001),
 (101101, 10221412201),
 (110011, 12102420121),
 (111111, 12345654321),
 (200002, 40000800004),
 (1000001, 1000002000001),
 (1001001, 1002003002001),
 (1002001, 1004006004001),
 (1010101, 1020304030201),
 (1011101, 1022325232201),
 (1012101, 1024348434201),
 (1100011, 1210024200121),
 (1101011, 1212225222121),
 (1102011, 1214428244121),
 (1110111, 1232346432321),
 (1111111, 1234567654321),
 (2000002, 4000008000004),
 (2001002, 4004009004004),
 (10000001, 100000020000001),
 (10011001, 100220141022001),
 (10100101, 102012040210201),
 (10111101, 102234363432201),
 (11000011, 121000242000121),
 (11011011, 121242363242121),
 (11100111, 123212464212321),
 (11111111, 123456787654321),
 (20000002, 400000080000004)]

b = []
def go(half_len):
  def check_and_put(v):
    num = int(v)
    r = check(num)
    if r:
      b.append(r)
  bound = 2**(half_len)
  for i in range(bound):
    v = bin(i)[2:].rjust(half_len, '0')
    rv = ''.join(reversed(v))
    num = '1' + v + rv + '1'
    check_and_put(num)
    for j in range(3):
      num = ''.join(['1', v, str(j), rv, '1'])
      check_and_put(num)
  v = '0' * half_len
  num = ''.join(['2', v, v, '2'])
  check_and_put(num)
  for j in range(3):
    num = ''.join(['2', v, str(j), v, '2'])
    check_and_put(num)

a = eval(open('C-table.txt').read())

import sys
import bisect
def main():
  nums = list(map(int, sys.stdin.read().split()))
  c = [x[1] for x in a]
  T = nums[0]
  for i in range(T):
    A, B = nums[2 * i + 1:2 * i + 3]
    #ans = sum(1 if (x[1] >= A) and (x[1] <= B) else 0 for x in a)
    ans = bisect.bisect(c, B) - bisect.bisect(c, A - 1)
    print("Case #" + str(i + 1) + ": " + str(ans))
main()
#for i in range(1, 27):
#  go(i)
#
#a = list(set(a + b))
#a.sort()
#print(a)
