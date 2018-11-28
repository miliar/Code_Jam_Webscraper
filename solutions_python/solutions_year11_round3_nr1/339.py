def solve_it(a,d,r,c):
    print "Case #%d:" % (d,)
    for i in range(0,r):
        for j in range(0,c):
            if a[i][j]=="#":
                try:
                  a[i][j]="/"
                  if a[i][j+1] =="#":
                      a[i][j+1]="\\"
                  else:
                      print "Impossible"
                      return
                  if a[i+1][j] =="#":
                      a[i+1][j]="\\"
                  else:
                      print "Impossible"
                      return 
                  if a[i+1][j+1] =="#":
                      a[i+1][j+1]="/"
                  else:
                      print "Impossible"
                      return
                except:
                  print "Impossible" 
                  return
    for i in range(0,r):
        s = ""
        for j in range(0,c):
            s = s + a[i][j]
        print s
    return
f = open("A-large.in","r")
c = 0
a = []
d = 0
for l in f:
    if c == 0:
        c = c + 1
        continue 
    if c==1:
        ab = l.strip("\n").split(" ")
        r = int(ab[0])
        rr =int(ab[0])
        cc = int(ab[1])
    else:
        r = r - 1
        if r>=0:
            a.append(list(l.strip("\n")))       
        else:
            d = d + 1
            solve_it(a,d,rr,cc)
            a = []
            ab = l.strip("\n").split(" ")
            r = int(ab[0])
            rr = int(ab[0])
            cc = int(ab[1])
    c = c + 1
d = d + 1
solve_it(a,d,rr,cc)
f.close()
