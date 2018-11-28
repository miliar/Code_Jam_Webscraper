
def a():
  f = file("test.in")
  d = f.read().split("\n")
  l = int(d[0])
  i = 0
  while i<l:
    dd = d[i+1].split(" ")
    smax = int(dd[0])
    people = []
    j = 0
    while j<smax+1:
      people.append(int(dd[1][j]))
      j = j+1
    i = i+1
    # solution
    p = people
    pi = 0
    pl = len(people)
    total_standing = 0
    friends_needed = 0
    while pi<pl:
      if (pi>total_standing):
        friends_needed = friends_needed + (pi-total_standing)
        total_standing = total_standing + (pi-total_standing)
      total_standing = total_standing + p[pi]
      pi = pi+1
    #print smax, people, friends_needed, total_standing
    print "Case #" + str(i) + ": " + str(friends_needed)
  return

