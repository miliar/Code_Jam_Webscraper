t = int(input())

c = 1

while t != 0:

  n = int(input())

  for i in range(n,0,-1):

    s = str(i)

    a = 0

    for j in range(len(s)-1):

      if int(s[j])>int(s[j+1]):

        a = 1

        break

    if a==0:
             print("Case #" + str(c) + ": " + str(i))

      c += 1

      break

  t -= 1