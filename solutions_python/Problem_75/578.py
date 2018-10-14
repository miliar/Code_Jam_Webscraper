#!/usr/bin/env python

filename = 'large.in'

def main():
  f = open(filename) 
  testcase_num = int(f.readline())
  for i in xrange(0, testcase_num):
    line = f.readline().strip().split()

    coms_num = int(line[0])
    coms = {}
    for j in xrange(1, 1 + coms_num):
      coms[line[j][0:2]] = line[j][2]
      coms[line[j][1::-1]] = line[j][2]
    # print coms

    opos_num = int(line[coms_num + 1])
    opos = {}
    for j in xrange(coms_num + 2, coms_num + 2 + opos_num):
      opos[line[j]] = 1
      opos[line[j][::-1]] = 1
    # print opos

    elements = line[coms_num + opos_num + 3]
    # print elements

    invoke = ''
    for e in elements:
      invoke = invoke + e
      # print invoke
      if len(invoke) > 1:
        if (invoke[-2:] in coms):
          # print 'Combine ' + invoke[-2:] + ' to ' + coms[invoke[-2:]]
          invoke = invoke[0:-2] + coms[invoke[-2:]]
        else:
          # print 'invoke[0:-1] = ' + invoke[0:-1]
          for o in invoke[0:-1]:
            if (o + e) in opos:
              # print 'Oppose ' + o + e
              invoke = ''
              break
    print 'Case #' + str(i+1) + ': [' + ', '.join(invoke) + ']'

if __name__ == '__main__':
  main()
