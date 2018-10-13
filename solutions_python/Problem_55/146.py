
def solve(firstLine,secondLine):
  r,k,n = int(firstLine[0]),int(firstLine[1]),int(firstLine[2])
  groups = [int(g) for g in secondLine]
  
  combi = []
  i = 0
  for g in groups:
    nbPeople = 0
    j = i
    while 1:
      tmp = groups[j%n]
      if nbPeople+tmp <= k:
        nbPeople += tmp
        j += 1
      else:
        break
      if j%n == i:
        break
    combi.append([nbPeople,j-i])
    i+=1
  
  visited = []
  people = []
  nbPeople = 0
  i = 0
  while 1:
    if i in visited:
      j = visited.index(i)
      cycleLength = len(visited)-j
      peoplePerCycle = nbPeople - people[j]
      remainingTimes = r - len(visited)
      fact = divmod(remainingTimes, cycleLength)
      nbPeople += (fact[0]*peoplePerCycle) + (people[j+fact[1]]-people[j])
      return nbPeople

    else:
      people.append(nbPeople)
      nbPeople += combi[i][0]
      visited.append(i)
      i = (i+combi[i][1])%n
      
    if len(visited) == r:
      return nbPeople
  
if __name__ == "__main__":
  i = 0
  for line in open("C-large.in"):
    if i > 0:
      if i%2 == 0:
        line2 = line.split()
        print "Case #%s: %s" % (i//2, solve(line1,line2))
      else:
        line1 = line.split()
    i += 1