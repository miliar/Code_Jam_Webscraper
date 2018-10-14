def is_palindrome(n):
  return n == int(str(n)[::-1])

outfile = open("out.txt", "w")
lines = open("input.txt", "r").read().split('\n')
cases = int(lines[0])
palindromes = [1, 4, 9, 121, 484]

for k in xrange(1, 25):
  # append odds
  for i in xrange(2**(k-1), 2**k):
    s = str(bin(i))[2:]
    for j in xrange(3):
      n = int(s + str(j) + s[::-1])
      if is_palindrome(n**2):
        palindromes.append(n**2)
  s = "2" + k * "0"
  n = int(s[:-1] + s[::-1])
  palindromes.append(n**2)
  s = "2" + (k-1) * "0" + "1"
  n = int(s[:-1] + s[::-1])
  palindromes.append(n**2)

  # append evens
  for i in xrange(2**k, 2**(k+1)):
    s = str(bin(i))[2:]
    n = int(s + s[::-1])
    if is_palindrome(n**2):
      palindromes.append(n**2)
  s = "2" + k * "0"
  n = int(s + s[::-1])
  palindromes.append(n**2)


for i in xrange(1, cases + 1):
  [x, y] = lines[i].split(' ')
  x = int(x)
  y = int(y)

  j = 0
  k = len(palindromes) - 1
  while x > palindromes[j]:
    j += 1
  while y < palindromes[k]:
    k -= 1
  outfile.write("Case #" + str(i) + ": " + str(k - j + 1) + "\n")
