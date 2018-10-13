def process_case(data, caseNo):
    people_to_invite = 0
    people_claping = data[0]
    for Si in range(1, len(data)):
        if Si > people_claping and data[Si] > 0:
            people_to_invite += Si - people_claping
            people_claping += people_to_invite
        people_claping += data[Si]
    print("Case #%s: %s" % (caseNo, people_to_invite))


with open('input.txt') as infile:
    lines = infile.readlines()

test_cases = int(lines[0])

for case in range(1, test_cases + 1):
    case_data = lines[case].strip()
    Smax, data = case_data.split()
    data = map(int, list(data))
    process_case(data, case)
