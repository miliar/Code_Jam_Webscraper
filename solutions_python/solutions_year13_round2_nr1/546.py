from Queue import Queue

def solve(armin, motes):
  motes = sorted(motes, reverse=True)
  q = Queue()
  q.put({'armin': armin, 'motes': motes, 'count': 0})
  while q.qsize > 0:
    state = q.get()
    
    while len(state['motes']) > 0 and state['armin'] > state['motes'][-1]:
      state['armin'] += state['motes'].pop()
    
    if len(state['motes']) == 0:
      return state['count']
    
    else:
      # Remove the biggest mote.
      newList = list(state['motes'])
      q.put({'armin': state['armin'], 'motes': newList[1:], 'count': state['count'] + 1})
      
      # Double armins size then take away one.
      q.put({'armin': state['armin'] + (state['armin'] - 1), 'motes': state['motes'], 'count': state['count'] + 1})

n = int(raw_input().strip())
for i in range(n):
  armin, nMotes = map(int, raw_input().split(' '))
  motes = map(int, raw_input().split(' '))
  print 'Case #%i: %i' % (i+1, solve(armin, motes))

