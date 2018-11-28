# Prob_B_small.py
f = open("B-small-attempt0.in","r")
Out = open("output.txt","w")
T = int(f.readline().replace("\n",''))

for z in range(1,T+1):
       N, V, T = f.readline().replace("\n",'').split(' ')
       N = int(N)
       V = float(V)
       T = float(T)

       Code = []
       for i in xrange(N):
              Code.append(f.readline().replace("\n",'').split(' '))
              Code[i][0] , Code[i][1] = float(Code[i][0]), float(Code[i][1])

       if N == 1:
              if Code[i][1] != T: Out.write("Case #" + str(z) + ": " + "IMPOSSIBLE" + "\n")
              else: Out.write("Case #" + str(z) + ": " + "%.9f" % (V / Code[i][0]) + "\n")
       elif N == 2:
              if T > Code[0][1] and T > Code[1][1]: Out.write("Case #" + str(z) + ": " + "IMPOSSIBLE" + "\n")
              elif T < Code[0][1] and T < Code[1][1]: Out.write("Case #" + str(z) + ": " + "IMPOSSIBLE" + "\n")
              elif T == Code[0][1] and T != Code[1][1]: Out.write("Case #" + str(z) + ": " + "%.9f" % (V / Code[0][0]) + "\n")
              elif T != Code[0][1] and T == Code[1][1]: Out.write("Case #" + str(z) + ": " + "%.9f" % (V / Code[1][0]) + "\n")
              elif T == Code[0][1] and T == Code[1][1]: Out.write("Case #" + str(z) + ": " + "%.9f" % (V / (Code[1][0] + Code[0][0])) + "\n")
              else:
                     if Code[1][1] > Code[0][1]:
                            Temp = Code[1][:]
                            Code[1] = Code[0][:]
                            Code[0] = Temp[:]
                     print Code
       
                     T0 = "%.9f" % (((V * (T - Code[1][1])) / Code[0][0]) / (Code[0][1] - Code[1][1]))
                     T1 = "%.9f" % ((V - (Code[0][0] * (((V * (T - Code[1][1])) / Code[0][0]) / (Code[0][1] - Code[1][1])))) / Code[1][0])
                     T0 = "%.9f" % (max(float(T0), float(T1)))
                     Out.write("Case #" + str(z) + ": " + T0 + "\n")
       
              
f.close()
Out.close()
