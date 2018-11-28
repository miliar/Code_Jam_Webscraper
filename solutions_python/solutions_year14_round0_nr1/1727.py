infile = 'A-small-attempt0.in'
outfile = 'A-small-out.txt'

def main():
  out = open(outfile, 'w')
  with open(infile) as f:
    N = int(f.readline())
    for n in xrange(N):
      guess1 = int(f.readline())
      nums1 = []
      for i in xrange(4):
        nums1.append(set(f.readline().split()))
      guess2 = int(f.readline())
      nums2 = []
      for i in xrange(4):
        nums2.append(set(f.readline().split()))
      possible = nums1[guess1-1] & nums2[guess2-1]
      if possible:
        if len(possible) == 1:
          out.write("Case #"+str(n+1)+": "+list(possible)[0]+" \n")
        else:
          out.write("Case #"+str(n+1)+": Bad magician!\n")
      else:
          out.write("Case #"+str(n+1)+": Volunteer cheated!\n")


main()

