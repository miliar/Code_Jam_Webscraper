#!/usr//bin/python

def mote(armin, motes, moves):
  if len(motes) == 0:
    return moves
  if armin > motes[0]:
    return mote(armin + motes[0], motes[1:], moves)
  if armin == 1:
    return mote(armin, motes[:-1], moves + 1)
  return min(mote(armin + armin - 1, motes, moves + 1), mote(armin, motes[:-1], moves + 1))

if __name__ == "__main__":
  n_cases = int(raw_input())
  for case in range(1,n_cases+1):
    armin = int(raw_input().split()[0])
    motes = [int(m) for m in raw_input().split()]
    motes.sort()
    moves = mote(armin, motes, 0)
    print "Case #%d: %d" % (case, moves)
