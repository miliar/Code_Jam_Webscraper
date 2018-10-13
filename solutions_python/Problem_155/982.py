def solve(input_str):
    counter = 0
    friends = 0
    input_str_part = input_str.split()
    shyness = int(input_str_part[0])
    audience_shyness_list = input_str_part[1]
    for i in range(shyness+1):
        if (counter < i):
            friends += 1
            counter += 1
        counter += int(audience_shyness_list[i])    

    return str(friends)

testcases = input()
    
for caseNr in xrange(1, testcases+1):
    cipher = raw_input()
    print("Case #%i: %s" % (caseNr, solve(cipher)))