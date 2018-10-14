import math

def Algorithm(stallnumber, personcount):
  if stallnumber == personcount:
    return [0, 0]
  else:
      stalls = []
      
      #add the first number to the stalls
      stalls.append(stallnumber)
      
      while personcount > 0:
        #choose the largest number
        current = max(stalls)
        stalls.remove(current)
        current += -1
        if current % 2 == 0:
          smax = current / 2
          smin = current / 2
        elif current == 1:
          smax = 1
          smin = 0
        else:
          smax = int(math.ceil(current/2))
          smin = int(math.ceil(current/2) -1)
          
        stalls.append(smax)
        stalls.append(smin)
        personcount += -1
        
      return [smax, smin]






###### thank god this isn't a beauty contest
k = open("input.txt", "r")
n = k.readlines()
k.close()


q = open("output.txt", "w")
ccount = 1
isfirst = True
for line in n:
    if isfirst:
        isfirst = False
    else:
        p = line.split(' ')
        stalls = int(p[0])
        people = int(p[1])
        f = Algorithm(stalls, people)
        q.writelines("Case #" + str(ccount) + ": " + str(int(f[0])) + ' ' + str(int(f[1])) + "\n")
        ccount += 1

q.close()


