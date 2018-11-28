def isTidy(s):
  for i in range(len(s) - 1):
    if s[i] > s[i + 1]:
      return False
  return True

def main():
  out = open('output.txt', 'w')
  with open('input.txt', 'r') as inp:
    tests = int(inp.readline())
    for test_number in range(1, tests + 1):
      found = False
      x = int(inp.readline())
      out.write('Case #%d: ' % test_number)
      sx = str(x)
      for i in range(len(sx), -1, -1):
        if not isTidy(sx[:i]):
          continue
        t = sx[:i]
        if len(t) > 0:
          d = t[-1]
          while len(t) < len(sx):
            t += d
          if t > sx:
            continue
        t = sx[:i]
        for j in range(i, len(sx)):
          for d in range(9, -1, -1):
            if t + (str(d) * (len(sx) - j)) > sx:
              continue
            t += str(d)
            break
        if t[0] == '0':
          t = t[1:]
        out.write(t + '\n')
        found = True
        break
  out.close()

if __name__ == '__main__':
  main()