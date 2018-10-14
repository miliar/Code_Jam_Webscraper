import math

"""
r = 10e14
s = int(math.sqrt(r)) + 1
i = 0
result = 0
testsP = 0
testsNP = 0
results = []
while i<s:
    i += 1
    sq = i**2
    sqt = str(sq)
    st = str(i)
    if st == st[::-1]:
        testsP += 1
	if sqt == sqt[::-1]:
            print "yes", i, sq
	    result += 1
	    results.append(sq)
    else:
	testsNP += 1
"""
# cached!
results = [1, 4, 9, 121, 484, 10201, 12321, 14641, 40804, 44944, 1002001, 1234321, 4008004, 100020001, 102030201, 104060401, 121242121, 123454321, 125686521, 400080004, 404090404, 10000200001L, 10221412201L, 12102420121L, 12345654321L, 40000800004L, 1000002000001L, 1002003002001L, 1004006004001L, 1020304030201L, 1022325232201L, 1024348434201L, 1210024200121L, 1212225222121L, 1214428244121L, 1232346432321L, 1234567654321L, 4000008000004L, 4004009004004L, 100000020000001L, 100220141022001L, 102012040210201L, 102234363432201L, 121000242000121L, 121242363242121L, 123212464212321L, 123456787654321L, 400000080000004L] 

# print result, testsP, testsNP
print results

text = open("C-large-1.in", "rt").readlines()
outfile = open("C-large-1.out", "wt")
tests = text[0]
cases = [line for line in text[1:]]
for idx,case  in enumerate(cases):
    bb = case.split(" ")
    low = int(bb[0])
    high = int(bb[1])
    temp = [r for r in results if r >= low and r <= high]
    num = len(temp)
    print "Case #", idx+1, ":", num, low, high
    outfile.write("Case #%s: %s\n" % (idx+1, num))

