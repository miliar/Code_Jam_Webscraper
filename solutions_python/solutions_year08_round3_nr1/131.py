def typing(P, K, L, F):
    assignment = {}
    for i in range(0, P + 1):
        assignment[i] = []
    keys = {}    
    pos = {}
    for k in range(1, K + 1):
        assignment[0].append(k)
        keys[k] = []
    
    feq = {}
    for letter in xrange(len(F)):
        f = F[letter]
        if not f in feq:
            feq[f] = []
        feq[f].append(letter)
    
    current = 0
    for feq_key in reversed(sorted(feq.keys())):
        frq = feq[feq_key]
        for letter in frq:
            if len(assignment[current]) == 0:
                current = current + 1
            key = assignment[current].pop()
            assignment[current + 1].append(key)
            keys[key].append(letter)
            pos[letter] = current + 1
            print "letter %s is assigned to key %s" % (letter, key)
            
    count = 0
    for letter in range(0, len(F)):
        number = F[letter]
        types = pos[letter]
        count = count + (types * number)
    return count

input_file = open("input.txt")
output_file = open("output.txt", "w")
case_count = int(input_file.readline())
for i in range(1, case_count + 1):
    output = None
    case1 = input_file.readline()
    case2 = input_file.readline()
    (P, K, L) = case1.split(" ")
    (P, K, L) = (int(P), int(K), int(L))
    F = case2.split()
    F = [int(e) for e in F]
    
    output = typing(P, K, L, F)
    
    print "=>", output
    output_line = "Case #%s: %s\n" % (i, output)
    output_file.writelines([output_line])
    