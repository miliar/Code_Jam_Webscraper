for case in xrange(1, input() + 1):
    num_wires = input()
    cordinates = [ [int(x) for x in raw_input().split()] for i in xrange(num_wires)]
#    print cordinates
    num_intesections = 0
    for i in xrange(num_wires):
        for j in xrange(i + 1, num_wires):
            if min(cordinates[i]) <= cordinates[j][0] <= max(cordinates[i]) and min(cordinates[i]) <= cordinates[j][1] <= max(cordinates[i]):
                num_intesections += 1
#                print cordinates[i], cordinates[j]
                continue
            if min(cordinates[j]) <= cordinates[i][0] <= max(cordinates[j]) and min(cordinates[j]) < cordinates[i][1] <= max(cordinates[j]):
                num_intesections += 1
 #               print cordinates[i], cordinates[j]
                continue
            for point in cordinates[j]:
                if min(cordinates[i]) <= point <= max(cordinates[i]) and (cordinates[i][0] -  cordinates[i][1]) * (cordinates[j][0] - cordinates[j][1]) < 0:
                    num_intesections += 1
  #                  print cordinates[i], cordinates[j]
                    break
    print 'Case #%i:' % case, num_intesections 
