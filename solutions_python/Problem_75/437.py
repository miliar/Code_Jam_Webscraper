def check_combine(combinations, e1, e2):
    for comb in combinations:
        match1 = comb.find(e1,0,2)
        match2 = comb.rfind(e2,0,2)
        if match1 != match2 and match1 != -1 and match2 != -1:
            return comb[-1]
    return ''

def check_oppose(oppositions, magick, e2):
    for oppose in oppositions:
        for element in magick:
            match1 = oppose.find(element)
            match2 = oppose.rfind(e2)
            if match1 != match2 and match1 != -1 and match2 != -1:
                return True
    return False
    
small_in = "B-large.in"
small_out = "B-large.out"

infile = open(small_in)
T = int(infile.readline().rstrip())
output = ""
for i in range(T):
    data = infile.readline().rstrip().split()
    C = int(data[0])
    D = int(data[C+1])
    N = int(data[-2])
    combinations = data[1:C+1]
    oppositions = data[C+2:C+2+D]
    invoke = data[-1]
    #Solve
    magick = []
    for j in range(N):
        if not magick:
            magick.append(invoke[j])
            print "next"
            continue
        e1 = magick[-1]
        e2 = invoke[j]
        combine = check_combine(combinations, e1, e2)
        if combine:
            magick[-1] = combine
        else:
            oppose = check_oppose(oppositions, magick, e2)
            if oppose:
                magick = []
            else:
                magick.append(e2)
    output += "Case #" + str(i+1) + ": ["
    for char in magick:
        output += char
        output += ", "
    output = output.rstrip(', ')
    output += "]\n"
    
outfile = open(small_out, 'w')
outfile.write(output)