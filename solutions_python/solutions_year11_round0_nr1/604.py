N = input()
for k in range(N):
  cs = raw_input().split()
  n = int(cs.pop(0))

  bots = dict(
    O = {'pos':1, 'target': 1, 'stack': []},
    B = {'pos':1, 'target': 1, 'stack': []})

  seq = []
  for c in cs:
    if c in 'OB':
      seq.append(c)
    else:
      bot = seq[-1]
      bots[bot]['stack'].append(int(c))
  #print seq
  #print bots

  ticks = 0
  
  while seq:
    ticks+=1
    next = seq[0]
    nope = 'B' if next == 'O' else 'O'

    bot = bots[next]
    other = bots['B'] if next == 'O' else bots['O']
    button = bot['stack'][0]
    bot['target'] = button
    if other['stack']:
      other['target'] = other['stack'][0]

    msg = {}
    if bot['pos'] == button:
      #bot['action'] = 'pushed'
      bot['stack'].pop(0)
      seq.pop(0)
      msg[next] = "self press button"
    elif bot['pos'] < button:
      bot['pos']+= 1
      msg[next] = "self move +1"
      #bot['action'] = 'moved'
    elif bot['pos'] > button:
      msg[next] = "self move -1"
      bot['pos']-=1
      #bot['action'] = 'moved'
      
    if other['target'] > other['pos']:
      other['pos']+=1
      msg[nope] = "other move +1"
    elif other['target'] < other['pos']:
      other['pos']-=1
      msg[nope] = "other move -1"
    else:
      msg[nope] = "other stay at %s" % other['pos']

    #print "%d O(%s) | B(%s)" % (ticks, msg['O'], msg['B'])
  print "Case #%d: %d" % (k+1, ticks)

