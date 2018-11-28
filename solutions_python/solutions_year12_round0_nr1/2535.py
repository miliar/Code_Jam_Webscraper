__author__ = 'danolsen'

input_one = "ejp mysljylc kd kxveddknmc re jsicpdrysi"
input_two = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"
input_three = "de kr kd eoya kw aej tysr re ujdr lkgc jv"

output_one = "our language is impossible to understand"
output_two = "there are twenty six factorial possibilities"
output_three = "so it is okay if you want to just give up"

mapping = {'z':'q', 'q':'z'}
for i in range(len(input_one)):
    mapping[input_one[i]] = output_one[i]

for i in range(len(input_two)):
    mapping[input_two[i]] = output_two[i]

for i in range(len(input_three)):
    mapping[input_three[i]] = output_three[i]

print mapping

f = open("A-small-attempt0.in", 'rb')
outfile = open("A-small-attempt0.out", 'w')

num_cases = int(f.readline())
print "Number of cases: %d" % num_cases

for i in range(num_cases):
    curr_line = f.readline()
    curr_line = curr_line.strip()
    #print curr_line

    output = ""
    for j in range(len(curr_line)):
        output = "%s%s" % (output, mapping[curr_line[j]])

    print output
    outfile.write("Case #")
    outfile.write("%d" % (i + 1))
    outfile.write(": ")
    outfile.write(output)
    outfile.write("\n")

f.close()
outfile.close()

#print mapping

#counter = 0
#for k, v in mapping.iteritems():
#    print "%d: %s = %s" % (counter, k, v)
#    counter += 1

#print mapping