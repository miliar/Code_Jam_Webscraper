import sys

def calculate_invites(audience):

    invites_total = 0
    audience_total = 0
    
    for i in range(len(audience)):
        audience_i = int(audience[i])
        invites_i = max(0, i - audience_total)
        audience_total = audience_total + audience_i + invites_i
        invites_total = invites_total + invites_i
            
    return invites_total

with open(sys.argv[1], 'r') as test_file:

    test_count = int(next(test_file))

    case_number = 1

    for line in test_file:

        max_shyness, audience_str = line.split()
        audience = list(audience_str)

        print("Case #{}: {}".format(case_number, calculate_invites(audience)))

        case_number = case_number + 1
