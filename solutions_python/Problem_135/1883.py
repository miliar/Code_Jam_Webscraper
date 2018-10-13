bad = "Bad magician!"
vc = "Volunteer cheated!"

def magic(m1, l1, m2, l2):
  r = set(m1[l1-1]) & set(m2[l2-1])
  if len(r) > 1:
    return bad
  if len(r) == 0:
    return vc
  return str(r.pop())

if __name__ == '__main__':
  import sys
  if len(sys.argv) > 1 and sys.argv[1] == 'tests':
    assert magic([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]], 2, [[1,2,5,4], [3,11,6,15], [9,10,7,12], [13,14,8,16]], 3) == '7'
    assert magic([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]], 2, [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]], 2) == bad
    assert magic([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]], 2, [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]], 3) == vc
  else:
    for t in range(int(raw_input())):
        l1 = int(raw_input())
        m1 = [map(int, raw_input().split()) for i in range(4)]
        l2 = int(raw_input())
        m2 = [map(int, raw_input().split()) for i in range(4)]
        print 'Case #%d: %s' % (t+1, magic(m1, l1, m2, l2))
