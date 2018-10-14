def getTestCases():    
    test = []    
    f = open("C-large.in", "r")
    n_line = 0
    n = 0
    while True:
      linea = f.readline()        
      if not linea: break
      if n_line != 0:
          t = linea.strip().split()
          test.append(t)                    
      else:
          n = linea.strip()        
      n_line = n_line + 1        
    f.close()
    return test, n

def recycle(n):
    rec = []
    for i in range(1,len(n)):
        rec.append(n[-1*i:] + n[:len(n)-i])
    return rec
    
tests, n = getTestCases()

case = 0
for e in tests:    
    total_count = 0
    exist = {}
    for n in range(int(e[0]),int(e[1])):    
        count = 0
        for m in recycle(str(n)):            
            if n<int(m) and int(m)<=int(e[1]) and len(str(n))==len(str(int(m))):
                if str(n)+","+m not in exist:
                    exist[str(n)+","+m] = True                    
                    count = count + 1                
                                                    
        total_count = total_count + count
    case = case + 1
    print "Case #"+str(case)+": "+ str(total_count)

    