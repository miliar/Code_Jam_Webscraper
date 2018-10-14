#!/usr/bin/python

f = open('A-small-attempt0.in')
inputline = f.readline()
numcase = int(inputline)

fout = open('speak_result.txt', 'w')

ref = {'a' : 'y',
  'b' : 'n',
  'c' : 'f',
  'd' : 'i',
  'e' : 'c',
  'f' : 'w',
  'g' : 'l',
  'h' : 'b',
  'i' : 'k',
  'j' : 'u',
  'k' : 'o',
  'l' : 'm',
  'm' : 'x',
  'n' : 's',
  'o' : 'e',
  'p' : 'v',
  'q' : 'z',
  'r' : 'p',
  's' : 'd',
  't' : 'r',
  'u' : 'j',
  'v' : 'g',
  'w' : 't',
  'x' : 'h',
  'y' : 'a',
  'z' : 'q'}
#ref = dict((v,k) for k, v in ref.iteritems())
invref = {}
for k, v in ref.iteritems():
  #print "k=",k," v=",v
  invref[v] = k
  #invref[v].append(k)

#for k, v in invref.iteritems():
#  print "k=",k," v=",v

#print invref
#print "ref:"
#print ref
for i in range (0,numcase):
  line = f.readline()
  #linelist = line.split()
  out = ""
  for j in range(0, len(line)):
    if line[j] == ' ':
      out = out + ' '
    elif line[j] == '\n':
      out = out + '\n'
    else:
      out = out + invref[line[j]]

  #print out
  answer = "Case #"+str(i+1)+": "+ out
  fout.write(answer)







f.close()
fout.close()

