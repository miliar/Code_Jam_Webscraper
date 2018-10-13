with open('input.txt') as f:
  n= int(f.readline())
  for i in range(n):
    needed = 0
    w,s = f.readline().split()
    #print s
    suma=0
    for j in range(len(s)):
        if s[j]=='0':
          continue
        needed += max(0,j-suma)
        suma = max(j,suma)
       	suma += int(s[j])
    print "Case #"+str(i+1)+": ",needed   
 
