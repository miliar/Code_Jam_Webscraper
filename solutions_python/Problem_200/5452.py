def digits_are_ascending(num):
    nstr = str(num)
    return all(int(x) <= int(y) for x, y in zip(nstr, nstr[1:]))

t = int(input())
for i in range(1, t + 1):
  line = input()
  n = int(line)
  while not digits_are_ascending(n):
      n -= 1

  #digits = str(line)[::-1]
  #pairs = [[int(x) for x in digits[y:y+2]] for y in range(0, len(digits))]
  #print(pairs)
  #answer = ''
  #for p, pair in enumerate(pairs):
  #    if len(pair) == 1 or pair != sorted(pair):
  #        answer += str(pair[0])
  #    else:
  #        answer += '9'
  #        if p < len(pairs) - 1:
  #            pairs[p+1][0] -= 1
  #answer = answer[::-1].lstrip('0')
  print("Case #{}: {}".format(i, n))


