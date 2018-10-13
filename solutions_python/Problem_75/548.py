
def parse(text):
    opposites = []
    combinations = []
    sequence = []

    items = text.split()
    pointer = 0
    comb_count = int(items[0])
    for comb in items[1:1+comb_count]:
        #print comb
        combinations.append((set(comb[:2]), comb[2]))

    pointer = comb_count + 1
    opp_count = int(items[pointer])
    for opp in items[pointer+1:pointer+1+opp_count]:
        opposites.append(set(opp))

    pointer = pointer + 1 + opp_count
    sequence = list(items[pointer+1])
    return opposites, combinations, sequence


def invoke(opposites=[], combinations=[], sequence=[]):
    for i in xrange(1, len(sequence)):
        for combination in combinations:
            #print set(sequence[i-1:i+1]), combination[0]
            if set(sequence[i-1:i+1]) == combination[0]:
                sequence[i-1] = combination[1]
                sequence[i] = '0'
                continue
        sub_seq = set(sequence[:i+1])
        for opposite in opposites:
            if opposite.issubset(sub_seq):
                #print sequence[:i+1], opposite, sub_seq
                sequence = ['0']*(i+1) + sequence[i+1:]
    sequence = filter (lambda a: a != '0', sequence)
    #print opposites, combinations, sequence
    #print "[%s]" %', '.join(sequence)
    return "[%s]" %', '.join(sequence)


#print invoke([], [(set("QR"), "I")], list("RRQR"))

#print parse("1 QRI 0 4 RRQR")
#print invoke(*parse("0 0 2 EA"))

file = open('B-large.in', 'rb')
outfile = open('B-large.out', 'wb')
items = file.readline()
for index, line in enumerate(file.readlines()):
    towrite = "Case #%s: %s\n" %( index+1, invoke(*parse(line)))
    outfile.write(towrite)