input_file = "C-large"
input_file += raw_input("Input file number and file extension:\n")
output_file = "outputClarge.txt"

max_power = 6
max_number = int(raw_input("Max number:\n")) #2223 #2000001
import collections

orbit_of = collections.defaultdict(int)#[0 for i in xrange(max_number)]
#num_unexplored = [True for i in xrange(max_number)]
num_orbits = 0
for n in xrange(max_number):
    if not orbit_of[n]:
        s = str(n)
        for i in range(len(s)):
            rotate = s[i:] + s[:i]
            if rotate[0] != '0':
                rotate = int(rotate)
                if rotate < max_number:
                    orbit_of[rotate] = num_orbits
                    #num_unexplored[n] = False
        num_orbits += 1
#print zip(xrange(100), orbit_of.itervalues())
#user = raw_input("wait")
print "Finished pre-loop generation."

inp = open(input_file, 'r')
out = open(output_file, 'w')
T = int(inp.readline())
for test in range(1, T + 1):
    orbit_sizes = collections.defaultdict(int)
    first, last = (int(item) for item in inp.readline().split())
    for n in xrange(first, last + 1):
        orbit_sizes[orbit_of[n]] += 1
        #if orbit_sizes[orbit_of[n]] == 4:
        #    print n
    num_pairs = 0
    #print list(orbit_sizes.itervalues())
    for size in orbit_sizes.itervalues():
        if size > 1:
            num_pairs += size * (size - 1) / 2
    out.write("Case #" + str(test) + ": " + str(num_pairs) + "\n")
    print test

out.close()
inp.close()
print "Done!"
