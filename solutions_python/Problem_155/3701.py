#getting data
data = input ()
print (data)
data = data.split('\n')
cases = int(data[0])
data = data [1:]
print (data)
for c in range (0, cases):
     data[c] = data[c].split()
     data[c][1] = data[c][1].split()        
print (data)

print (data[0][1][0][0])



for c in range (0, cases):
     shy = 0
     friends = 0
     for n in range (0, int(data[c][0])+1):
          if shy < n:
               friends += n - shy
               shy += n - shy
          shy += int(data[c][1][0][n])
     print ("Case #" + str(c+1) + ": " + str(friends))
