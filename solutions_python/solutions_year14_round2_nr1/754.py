fname = 'A-small-attempt5'
fin = open('%s.in' % fname,'r')
fout = open('%s.out' % fname,'w')

T = int(fin.readline())

for i in range(T):
  Nw = int(fin.readline())
  words = [fin.readline().strip('\n') for x in xrange(Nw)]
  print words
  
  letters = list(set(words[0]))
  Nl = len(letters)
  same_letters = True
  for word in words:
    if set(word) != set(letters):
      same_letters = False
      break
  
  if same_letters == False:
    fout.write('Case #%u: Fegla Won\n' % (i+1))
    continue
  
  # letnum = [[0 for x in xrange(Nw)] for x in xrange(Nl)] 
  # for l in range(Nl):
    # for w in range(Nw):
      # letnum[l][w] = words[w].count(letters[l])
  # print letters
  # print letnum
  
  
  
  
  score = 0
  isvalid = True
  # for l in range(Nl):
  while len(words[0]) > 0:
    letter = words[0][0]
    print 'LETTER %s' % letter
    letteri = [0]*Nw
    lweight = [1]*Nw
    for w in range(Nw):
      word = words[w]
      if len(word) == 0 or word[0] != letter:
        isvalid = False
        break
      
      letidx = 0
      while letidx < len(word) and word[letidx] == letter:
        letteri[w] += 1
        letidx += 1
      words[w] = words[w][letidx:]
      # print 'words[%u]=%s' % (w,words[w])
      
    if isvalid == False:
      break
      
    while len(letteri) > 1:
      print 'letteri = %s' % letteri
      print 'lweight = %s' % lweight
      idx = [x[0] for x in sorted(enumerate(letteri), reverse=True, key=lambda x:x[1])]
      print 'idx = %s' % idx
      
      scorel = lweight[idx[0]]*abs(letteri[idx[0]]-letteri[idx[1]])
      scores = lweight[idx[-1]]*abs(letteri[idx[-2]]-letteri[idx[-1]])
      if scorel < scores:
        print 'add scorel=%u (%u,%u)' % (scorel,idx[0],idx[1])
        score += scorel
        lweight[idx[1]] += lweight[idx[0]]
        del lweight[idx[0]]
        del letteri[idx[0]]
      else:
        print 'add scores=%u (%u,%u)' % (scores,idx[-1],idx[-2])
        score += scores
        lweight[idx[-2]] += lweight[idx[-1]]
        del lweight[idx[-1]]
        del letteri[idx[-1]]
    
    print '\n'
      
  print '\n'
  
  if isvalid:
    for word in words:
      if len(word) > 0:
        isvalid = False
        break
  
  if isvalid:
    fout.write('Case #%u: %0.9g\n' % (i+1,score))
  else:
    fout.write('Case #%u: Fegla Won\n' % (i+1))

fin.close()
fout.close()