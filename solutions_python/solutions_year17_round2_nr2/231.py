file_in = open('b1.in', 'r')
file_out = open('b.out', 'w')

colors = {
  'R': 1,
  'O': 3,
  'Y': 2,
  'G': 6,
  'B': 4,
  'V': 5
}

def check(order):
  n = len(order)
  for i in range(n-1):
    if colors[order[i]] & colors[order[i+1]] > 0:
      return False
  if colors[order[0]] & colors[order[n-1]] > 0:
    return False
  return True

T = int(file_in.readline())

for t in range(1, T+1):
  n, r, o, y, g, b, v = map(int, file_in.readline().split())
  ans = []

  if o > b:
    ans = 'IMPOSSIBLE'
  elif g > r:
    ans = 'IMPOSSIBLE'
  elif v > y:
    ans = 'IMPOSSIBLE'
  else:
    b -= o
    r -= g
    y -= v

    if b > r + y or r > b + y or y > r + b:
      ans = 'IMPOSSIBLE'
    else:
      m = max(b, r, y)
      ans = ''
      if m > 0:
        if(b == m):
          ans = 'B'
          b -= 1
        elif(r == m):
          ans = 'R'
          r -= 1
        elif(y == m):
          ans = 'Y'
          y -= 1
      while(b + r + y > 0):
        # find the largest number that's not the last 
        if ans[-1] == 'B':
          if r > y:
            ans += 'R'
            r -= 1
          else:
            ans += 'Y'
            y -= 1
        elif ans[-1] == 'R':
          if b > y:
            ans += 'B'
            b -= 1
          else:
            ans += 'Y'
            y -= 1
        elif ans[-1] == 'Y':
          if r > b:
            ans += 'R'
            r -= 1
          else:
            ans += 'B'
            b -= 1

      # for the color G:
      if g > 0:
        if ans == '':
          ans = 'RG' * g
        else:
          # find the first instance of R
          for i in range(len(ans)):
            if ans[i] == 'R':
              break
          ans = ans[:i] + 'RG' * g + ans[i:]
      if o > 0:
        if ans == '':
          ans = 'BO' * o
        else:
          # find the first instance of R
          for i in range(len(ans)):
            if ans[i] == 'B':
              break
          ans = ans[:i] + 'BO' * o + ans[i:]
      if v > 0:
        if ans == '':
          ans = 'YV' * v
        else:
          # find the first instance of R
          for i in range(len(ans)):
            if ans[i] == 'Y':
              break
          ans = ans[:i] + 'YV' * v + ans[i:]

  if ans is not 'IMPOSSIBLE':
    if ans[-1] == ans[0]:
      ans = ans[:-2] + ans[-1] + ans[-2]

    if check(ans) == False:
      print('Test failed for test case ', t)

  file_out.write("Case #{}: {}\n".format(t, ans))