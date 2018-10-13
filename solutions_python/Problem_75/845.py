
T = int(raw_input())

for c in range(1, T+1):
  line = raw_input().split()
  
  n_base = int(line[0])
  comb = {}
  for i in range(1, n_base+1):
    l = list(line[i][0:2])
    l.sort()
    assert len(line[i]) == 3
    comb[tuple(l)] = line[i][-1]
  opp = set([])
  for j in range(1, int(line[1+n_base])+1):
    assert len(frozenset(tuple(line[1+n_base+j]))) == 2
    opp.add(frozenset(tuple(line[1+n_base+j])))
  
  current_list = []
  ellist = list(line[-1])
  
  #print comb, opp, ellist
  while ellist:
    action = ellist.pop(0)
    current_list.append(action)
      
    # combine
    found = True
    while found:
      found = False
      for i in range(len(current_list)-1, -1, -1):
        l = current_list[i:]
        assert len(l) > 0
        l.sort()
        l = tuple(l)
        if l in comb: 
          del_list = current_list[i:]
          current_list = current_list[0:i]
          current_list.append(comb[l])
          found = True
          break
      
    # opposite
    for j in range(0, len(current_list)):
      if not current_list:
        break
      for i in range(0, len(current_list)):
        if i != j:
          s1 = frozenset([current_list[j], current_list[i]])
          if s1 in opp:
            current_list = []
            break
  
  #print comb, opp, line[-1]
  print 'Case #%d: [%s]' % (c, ', '.join(current_list))

