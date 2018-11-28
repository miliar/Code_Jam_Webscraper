from fractions import gcd
filename_prefix = "A-large"
#filename_prefix = "A-small-attempt%d" % 1
infile = open("%s.in"%filename_prefix)
outfile = open("%s.out"%filename_prefix,'w')
cases = int(infile.readline())
offset = 0

for case in range(1, cases+1):
    n,Pd,Pg = map(int,infile.readline().split())
    D = 100/gcd(Pd,100)
    if D>n or (Pg!=Pd and (Pg==100 or Pg==0)):
        Broken = True
    else:
        Broken = False
    if Broken:
        outfile.write( "Case #%d: Broken\n" % case)
    else:
        outfile.write( "Case #%d: Possible\n" % case)
    
infile.close()
outfile.close()
