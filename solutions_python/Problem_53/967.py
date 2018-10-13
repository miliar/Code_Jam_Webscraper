import sys

fin = sys.stdin

def change_status(status_neigbord, status):
  if status_neigbord == "ON":
    if status == "OFF":
      return "ON"
    else:
      return "OFF"
  else:
    return status

for case in range(1, int(fin.readline()) + 1):
  N, K = map(int, fin.readline().split())
  #print N, ":", K
  snappers = ["OFF" for x in range(0,N)]
  for i in range(0,K):
    #print i
    snappers_copy = list(snappers)
    #print i,":", snappers_copy
    for j in range(0, N):
      if j == 0 and snappers_copy[0] == "OFF":
        snappers[0] = "ON"
        break
      elif j == 0 and snappers_copy[0] == "ON":
        snappers[0] = "OFF"
      elif j > 0 and snappers_copy[j-1] == "OFF":
        snappers[j-1] = "ON"
        break 
      else:
        snappers[j] = change_status(snappers_copy[j-1], snappers_copy[j])
      #print j,snappers
  if "OFF" in snappers:
    print "Case #%d: %s" % (case, "OFF")
  else:
    print "Case #%d: %s" % (case, "ON")

