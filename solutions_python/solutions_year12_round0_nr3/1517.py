def rotate():
  f = open('C-small-attempt0.in', 'r')
  #f = open('test2.txt', 'r')
  N = f.readline()
  i = 1
  for line in f:
    ans = 0
    spl = line.split(' ')
    A = int(spl[0])
    B = int(spl[1])
    str1 = spl[0]
    while (A < B):
      for j in range(len(str1)-1):
        temp = str1[-1] + str1[0:len(str1)-1]
        if int(temp)<=B and int(temp)>A:
          ans = ans+1 
        str1 = temp          
      A = A + 1
      str1 = str(A)
    print "Case #" + str(i) + ": " + str(ans)
    i += 1
  


rotate()