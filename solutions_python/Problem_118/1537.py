import sys, re

def isqrt(n):
    x = n
    y = (x + n // x) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

T = int(input())
out = ""
f = open('out.txt', "w")
for t in range(T):
  count = 0
  line = sys.stdin.readline().split()

  if(isqrt(int(line[0]))**2<int(line[0])):
    minim = isqrt(int(line[0]))+1
  else:
    minim = isqrt(int(line[0]))
  maxim = isqrt(int(line[1]))
  if(int(line[0])<=9 and int(line[1])>=9):
    count = count+1
  i = minim
  while i <= maxim:
    mt2 = str(i).find('3')
    if(mt2 != -1):
      i += 7*10**(len(str(i))-mt2-1)
    else:
      if(str(i) == str(i)[::-1]):
        if(str(i**2) == str(i**2)[::-1]):
          # print(i)
          count += 1
      i += 1;
  out += "Case #"+str(t+1)+": "+str(count)+"\n"
f.write(out)