# Max best result for non-surprising triplet is floor((total-1)/3 + 1)
# Max best result for surprising triplet is floor((total-2)/3 + 2)
# Cutoff total for non-suprising triplet is (p-1)*3+1
# Cutoff total for suprising triplet is (p-2)*3+2
# This doesn't work for very small p
# non-s cutoff for p = 1 is 1
# non-s cutoff for p = 0 is 0
# s cutoff for p = 1 is 1
# s cutoff for p = 0 is 0

# Algorithm:
# Set counter for result to 0
# Discard all below cutoff total for suprpising triplet
# Remove all at or above the cutoff for non-suprising triplets and add number to result
# Add the lesser of the number of suprising triplets and the remaining totals to the result
# Return result

def process_line(line):
    parts = [int(x) for x in line.split(" ")]
    n = parts.pop(0)
    s = parts.pop(0)
    p = parts.pop(0)
    totals = parts[:n]
    
    result = 0
    if p>1:
        n_cutoff=(p-1)*3+1
        s_cutoff=(p-2)*3+2
    else:
        n_cutoff=p
        s_cutoff=p
    #print n_cutoff,s_cutoff
    #print totals
    totals = filter(lambda score: score >= s_cutoff,totals)
    #print totals
    result += len(filter(lambda score: score >= n_cutoff,totals))
    totals = filter(lambda score: score < n_cutoff,totals)
    #print totals
    if len(totals) > s:
        result += s
    else:
        result += len(totals)
    return result


inputfile='B-large.in'
input = [line.strip() for line in open(inputfile).readlines()]

t = int(input.pop(0))

for i in range(t):
    #print input[i]
    print "Case #%i: %i" % (i+1,process_line(input[i]))
