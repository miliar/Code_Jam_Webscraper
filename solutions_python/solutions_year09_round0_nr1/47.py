import re

file = "./A-large"
fd = open(file + ".in","r")

param = fd.readline()
params = param.split(" ")

dic = []
for i in range(int(params[1])):
    dic += [fd.readline().strip()]
  
patterns = []
for i in range(int(params[2])):
    patterns += [fd.readline().strip()]
    
fd.close()
    
case = "Case #No:"
no = 1
count = 0

output = ""
for pattern in patterns:
    for word in dic:
        pattern = re.sub("\(","[",pattern)
        pattern = re.sub("\)","]",pattern)
        b = re.match(pattern, word)
        if not b == None:
            count += 1
    c = case.replace("No", str(no))
    no += 1
    output += c + " " + str(count) + "\n"
    count = 0
    
fd = open(file + ".out", "w")
fd.write(output)
fd.close
#fd.open(file + ".out", "w")    
    
#b = re.match("[ab][bc][ca]", "ab")
