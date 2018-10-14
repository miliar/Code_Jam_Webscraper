# Python - KBS
import fileinput

if __name__ == '__main__':
  cases = None
  friends = 0

  for case, line in enumerate(fileinput.input()):
    # reset friend counter
    friends = 0

    data = line.strip().split(' ')

    # first line is number of cases
    if case == 0:
      cases = int(data[0])
      continue

    # handle the string
    smax = int(data[0])
    ##
    peopleUp = 0
    for idd, noo in enumerate(data[1]):
      # check if already enough are up
      if peopleUp >= idd:
        peopleUp += int(noo)
      else:
        newFriends = (idd - peopleUp)
        friends += newFriends
        peopleUp += newFriends + int(noo)
    
    print "Case #%d: %d" % (case, friends)
