fname = 'A-small-attempt1'
fin = open('%s.in' % fname,'r')
fout = open('%s.out' % fname,'w')

T = int(fin.readline())

for i in range(T):
  r1 = int(fin.readline())
  cards1 = [fin.readline().strip('\n').split(' ') for x in xrange(4)]
  r2 = int(fin.readline())
  cards2 = [fin.readline().strip('\n').split(' ') for x in xrange(4)]
  
  common = set(cards1[r1-1]) & set(cards2[r2-1])
  num_common = len(common)
  
  # retval = {0: 'Bad magician!', 1:common.pop()}.get(num_common, 'Volunteer cheated!')
  # fout.write('Case #%u: %s\n' % (i,retval))
  if num_common > 1:
    fout.write('Case #%u: Bad magician!\n' % (i+1,))
  elif num_common < 1:
    fout.write('Case #%u: Volunteer cheated!\n' % (i+1,))
  else:
    fout.write('Case #%u: %s\n' % (i+1,common.pop()))

fin.close()
fout.close()