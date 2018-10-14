def solverec(pos, arr, constrained, mindigit, cache):
  if (pos,mindigit) in cache:
    return cache[(pos,mindigit)]

  if pos == len(arr):
    return []
  if not constrained:
    return [9] * (len(arr) - pos)
  #if pos == len(arr) - 1:
  #  return [arr[pos]]
  if mindigit > arr[pos]:
    return None
  
  rec1 = solverec(pos+1, arr, True, max(mindigit,arr[pos]),cache)
  rec2 = None
  if arr[pos] - 1 >= mindigit:
    rec2 = solverec(pos+1, arr, False, max(mindigit,arr[pos]-1),cache)
  if rec1 is not None:
    res = [arr[pos]] + rec1
  elif rec2 is not None:
    res = [arr[pos]-1] + rec2
  else:
    return None
  cache[(pos,mindigit)] = res
  return res
  #minright = min(arr[pos+1:])
  #if arr[pos] <= minright:
  #  return [arr[pos]]  + solverec(pos+1, arr, True)
  #else:
  #  return [arr[pos]-1] + solverec(pos+1, arr, False)
  
def solve(input):
  cache = dict()
  return int("".join([str(i) for i in solverec(0, [int(ch) for ch in input],True,0,cache)]),10)
 
def main():
  name = "B-large"
  lines = open(name+'.in').read().split("\n")
  out = []
  for i, line in enumerate(lines[1:]):
    if len(line) > 0:
      out.append("Case #%d: %d" % (i+1, solve(line)))

  open(name+'.out','w').write("\n".join(out))
    
main()