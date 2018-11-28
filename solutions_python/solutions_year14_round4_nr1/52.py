def solve(cap, sizes):
  sizes.sort(reverse=True)
  #print sizes
  #print cap
  done = [False for f in sizes]
  p = 0
  count = 0
  while p < len(done):
    # If the file has been included already, skip it
    if done[p]:
      p += 1
      continue
    # The file has not been included, so find the pointer to the largest
    # file, if any, that will fit in the remaining space for this file
    q = p + 1
    while q < len(done):
      if done[q]:
        q += 1
        continue
      if sizes[p] + sizes[q] <= cap:
        break
      q += 1
    if q != len(done):
      # We found another file that will fit, mark it as done
      done[p] = True
      done[q] = True
      #print (sizes[p], sizes[q])
    else:
      done[p] = True
      #print (sizes[p],)
    # Increase the result and move on to the next file
    count += 1
    p += 1
  return count

for tc in range(int(raw_input())):
  cap = int(raw_input().split(" ")[1])
  sizes = [int(size) for size in raw_input().split(" ")]
  print "Case #" + str(tc + 1) + ": " + str(solve(cap, sizes))
