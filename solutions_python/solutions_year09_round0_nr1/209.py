(L, D, N) = map(int, raw_input().split())
dict = set()
for i in xrange(D):
  dict.add(raw_input())
 
#print dict
for case in xrange(N):
#  print "starting case #"+str(case+1)
  pos = 0
  letters = raw_input()
  words = dict.copy()
  inparens = False
  for letter in letters:
#    print 'processing ' + letter
#    print words
    if letter == '(':
      theseparens = []
      inparens = True
    elif letter == ')':
      toremove = set()
      for word in words:
        if word[pos] not in theseparens:
          toremove.add(word)
      inparens = False
      words.difference_update(toremove)
      pos += 1
    else:
      if not inparens:
        toremove = set()
        for word in words:
          if word[pos] != letter:
            toremove.add(word)
        #print 'toremove ' + str(toremove)
        words.difference_update(toremove)
        #print 'done: '
        #print words
        pos += 1
      else:
        theseparens.append(letter)

  print "Case #" + str(case+1) + ": " + str(len(words))
#  print words

