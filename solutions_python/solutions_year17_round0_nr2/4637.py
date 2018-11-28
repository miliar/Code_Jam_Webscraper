def runAlgorithm(upto):
    #tidy numbers bollocks
    def isTidy(num):
      if len(str(num)) != 1:
        m = 0
        while m < len(str(num)) - 1:
          if int(str(num)[m]) <= int(str(num)[m+1]) :
            m += 1
          else:
            return False
        return True
      else:
        return True
      
    lasttidy = 0
    while lasttidy == 0:
      if isTidy(upto):
        lasttidy = upto
      else:
        upto = upto -1
    return lasttidy



k = open("test.txt", "r")
n = k.readlines()
print(n)
k.close()

m = open("output.txt", "w")
isfirst = True
ccount = 1
for doodaa in n:
    if isfirst:
        isfirst = False
    else:
        m.writelines("Case #" + str(ccount) + ": "+ str(runAlgorithm(int(doodaa))) + "\n")
        ccount += 1
m.close()

