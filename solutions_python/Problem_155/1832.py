def main():
  T = int(raw_input())
  for c in xrange(T):
    (Smax, audience) = raw_input().split()
    standing = 0
    added = 0
    for i in xrange(int(Smax)+1):
      if standing < i:
        added = added + 1
        standing = standing + 1
      standing = standing + int(audience[i])
    print "Case #%d: %d" % (c+1, added)

if __name__ == "__main__":
  main()
