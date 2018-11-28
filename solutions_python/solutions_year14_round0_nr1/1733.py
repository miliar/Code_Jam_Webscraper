def data(filename):
    f = open(filename,"r")
    o = open(filename + ".out","w")    
    test = f.readline()
    t = f.readlines()
    for i in range(0,int(test.strip())):
         a = set((t[int(t[10*i])+i*10].strip()).split())
         print t[10*i]
         print a
         b = set((t[int(t[10*i+5])+i*10+5].strip()).split())
         print t[10*i+5]        
         print b
         if (len(a.intersection(b)) == 0):
             o.write("Case #" + str(i+1) + ": Volunteer cheated!\n")
         elif (len(a.intersection(b)) == 1):
             o.write("Case #" + str(i+1) + ": " + str((a.intersection(b)).pop()) + "\n")
         else:
             o.write("Case #" + str(i+1) + ": Bad magician!\n")
    f.close()
    o.close()