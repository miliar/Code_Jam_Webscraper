import fileinput
inp = []
for line in fileinput.input():
    inp.append(line)
    
test_cases = int(inp[0])
results = []
case = 0
while case < test_cases:
    #get the next test case; setup data
    current_case = inp[case+1].split(' ')
    maxShyness = current_case[0]
    audience_string = list(current_case[1])
    audience = [int(x) for x in audience_string if x != '\n']
    #
    standing = 0
    for i in range(len(audience)):
        if( i == 0 ):
            standing += audience[i]
        else:
            if( i > standing ):
                standing += i - standing
            standing += audience[i]
             
    results.append(standing - sum(audience))
    #result[case] should be the # of people in total # needed - # in audience 
    case += 1
    
for r in range(len(results)):
    print("Case #" + str(r+1) + ": " +  str(results[r]) )