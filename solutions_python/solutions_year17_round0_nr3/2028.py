def read_input_file(fileName_in):
    fo = open(fileName, "r")
    content = fo.read().strip()
    fo.close()
    
    lines = content.split("\n")
    tc = lines[0]
    lines = lines[1:]
    
    return(tc, lines)

def Compute(N,K):
    people = list()
    people.append(0)
    people.append(N+1)
    person_index = (N + 1)
    list_index = 1
    for i in range(K):
        Npi = 0
        Nci = people[1]
        gi1 = Npi
        gi2 = Nci
        max_gap = gi2 - gi1
        list_index = 1
        for j in range(1,len(people)):            
            Nci = people[j]            
            g1 = Nci - Npi
            if g1 > max_gap:
                gi1 = Npi
                gi2 = Nci
                max_gap = gi2 - gi1
                list_index = j
            Npi = Nci

        #print(Npi, Nci)
        

        person_index = gi1 + int((max_gap) / 2)        
        people.insert(list_index, person_index)
        #print(people, list_index)
    #print(person_index)
    #print(list_index)
    #print(people)
    left = people[list_index - 1]
    right = people[list_index + 1]
    #print(left, list_index, right)
    ls = person_index - left - 1
    rs = right - person_index - 1
    val = (max(ls,rs), min(ls,rs))
    #print(val)
    return val

#fileName = "Test.txt"
fileName = "small.in"
#fileName = "large.in"

(tc, lines) = read_input_file(fileName)

outFile = list()
case = 0

for l in lines:
    (N,K) = l.strip().split(" ")
    result = Compute(int(N),int(K))
    case += 1
    outFile.append("Case #" + str(case) + ": " + str(result[0]) + " " + str(result[1]))
#print("\n".join(outFile))

fo = open(fileName + ".out.txt", "w")
fo.write("\n".join(outFile))
fo.close()
