
num_cases = int(raw_input())

def recurse(motes, a):
  a_prev = 0
  new_motes = motes
  while a_prev != a:
    a_prev = a
    a += sum([m for m in new_motes if m < a])
    new_motes = [m for m in new_motes if m >= a_prev]

  if len(new_motes) == 0:
    return 0

  if a <= 1:
    return len(motes)

  ma = max(new_motes)
  d_motes = new_motes[:new_motes.index(ma)] + new_motes[new_motes.index(ma)+1:]
  return 1 + min(recurse(d_motes, a), recurse(new_motes[:], a*2-1))


for casenum in range(1, num_cases+1):
  A, N = map(int, raw_input().split(" "))
  motes = map(int, raw_input().split(" "))
  def get_ans():
    global motes, A, N
    return recurse(motes[:], A)
    # count = 0
    # a = A
    # while len(motes) > 0:
    #   print a, motes
    #   a_prev = a
    #   a += sum([m for m in motes if m < a])
    #   motes = [m for m in motes if m >= a_prev]
    #   if a == a_prev:
    #     count += 1
    #     # see how it plays out:
    #     n = a * 2 - 1
    #     n_prev = 0
    #     while n_prev != n:
    #       n_prev = n
    #       n += sum([m for m in motes if m < n])
    #     if n > max(motes):
    #       return count + 1
    #     # a is smaller than all in list
    #     if a + a - 1 + sum(motes) - max(motes) > 0 or a <= 1:
    #       del motes[motes.index(max(motes))]
    #     else:
    #       motes += [a-1]
    return count

  ans = get_ans()
  print "Case #%d: %s" % (casenum, ans)