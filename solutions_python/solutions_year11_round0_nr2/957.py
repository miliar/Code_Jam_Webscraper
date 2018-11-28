#!/usr/bin/python

def readfile(file):
  """
    input:

    T (number of test cases)
    C t D o N s

    t - transformation strings (3 char)
    o - oppositions (2 char)
    s - series (N char)
  """

  tests = []

  numtests = file.readline().strip()

  T = int(numtests)

  for i in xrange(T):
    line = file.readline().strip()

    parts = line.split(" ")

    index = 0

    C = int(parts[index])
    index = index + 1

    t = {}

    for j in xrange(C):
      trans = parts[index]
      index = index + 1

      target = trans[2]
      one = trans[0]
      other = trans[1]

      o12 = "%s%s" % (one, other)
      o21 = "%s%s" % (other, one)

      t[o12] = target
      t[o21] = target

    D = int(parts[index])
    index = index + 1

    o = {}

    for j in xrange(D):
      oppose = parts[index]
      index = index + 1

      one = oppose[0]
      other = oppose[1]

      if one in o:
        o[one].append(other)
      else:
        o[one] = [other,]

      if other in o:
        o[other].append(one)
      else:
        o[other] = [one,]

    N = int(parts[index])
    index = index + 1

    series = parts[index]
    s = list(series)

    tests.append( { 'transformations' : t, 'oppositions' : o, 'series': s } )

  return tests

def invoke(element_list, trans, opps, element):
  # Add it to the list
  element_list.append(element)

#  print "list: %s" % (element_list, )

  # Check combinations
  if len(element_list) > 1:
    last = element_list[-2:]

    last = "".join(last)

    if last in trans:
      # get translation
      t = trans[last]

      # remove last two
      element_list = element_list[:-2]

      # add translation
      element_list.append(t)

#      print "trans: %s" % (element_list, )

  # Check oppositions
  if len(element_list) > 0:
    last = element_list[-1]
#    print "last = %s" % (last, )

    if last in opps:
#      print "here: %s" % (element_list[:-1])
#      print "opp: %s" % (opps[last])
      # it has an opposition
      for opp in opps[last]:
        if opp in element_list[:-1]:
          # clear list
          element_list = []

#          print "cleared: %s" % (element_list, )

          break

  # done
  return element_list

def run(test):
  trans = test['transformations']
  opps = test['oppositions']
  series = test['series']

  element_list = []

  for element in series:
    element_list = invoke(element_list, trans, opps, element)

  return element_list

def display(result):
  return "[%s]" % (", ".join(result), )

file = open("B-large.in.txt", "rt")

tests = readfile(file)

case = 1

for test in tests:
#if True:
##  test = tests[2]
  result = run(test)
  print "Case #%d: %s" % (case, display(result))
  case = case + 1

file.close()
