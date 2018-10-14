#!/usb/bin/python
colors = {'O':0,'B':1}

def solve(a):
  t = 0
  pos = [1, 1]
  spare,lastcolor=0,-1
#  print str(len(a)/2) + " buttons to click"
  for i in range(len(a)/2):
#    print t, pos, spare, lastcolor
    color = colors[a[2*i]]
    target = int(a[2*i+1])
#    print color, target
    if color == lastcolor:
      delta = abs(pos[color]-target) + 1
#      print "delta", delta
      t += delta
      spare += delta
    else: 
      delta = spare - abs(pos[color]-target)
      if delta >= 0:
        t += 1
        spare = 1
      else:
        t += abs(delta) + 1
        spare = abs(delta) + 1
    pos[color] = target
    lastcolor = color
  return t
  

if __name__ == '__main__':
  f = open('A-large.in', 'r')
  T = int(f.readline().rstrip());
  for t in range(1,T+1):
    a = solve(f.readline().split()[1:])
    print "Case #" + str(t) + ":", a
  
