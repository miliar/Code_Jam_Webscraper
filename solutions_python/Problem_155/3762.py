# Standing ovation

tests = int(raw_input())

for case in range(0, tests):
    s_max, audience = raw_input().split()
    s_max = int(s_max)+1

    current = 0
    missing = 0
    for step in range(0, s_max):
        standing = current+missing
        currPerson = int(audience[step])
        if step <= standing:
            current += currPerson
        elif currPerson != 0 and step>standing:
            missing += step-standing
            current += currPerson
            
    print "Case #"+str(case+1)+": "+str(missing)

