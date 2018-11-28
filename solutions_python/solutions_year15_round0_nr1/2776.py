prefix = "A-large"
postfixIn = ".in"
postfixOut = ".out"

fileIn = open(prefix + postfixIn, "r")
lines = fileIn.readlines()
fileIn.close()

results = []
template = "Case #%d: %s\n"

############################################################

# find the number of additional friends for all the audience to stand
def count_additional_friends(audience):
    if len(audience) < 2:
        return 0

    additional_friends = 0
    number_standing = audience[0]
    for shyness in xrange(1, len(audience)):
        friends_required = shyness - number_standing
        if friends_required > 0:
            additional_friends += friends_required
            number_standing += friends_required
        number_standing += audience[shyness]

    return additional_friends

line_number = 0
case_no = 1
for line in lines:
    line_number += 1
    if line_number <= 1:
        continue

    line.strip()
    tokens = line.split()
    audience = [int(s) for s in tokens[1]]

    results.append(template % (case_no, count_additional_friends(audience)))
    case_no += 1

############################################################

fileOut = open(prefix + postfixOut, "w")
for result in results:
    fileOut.write(result)
fileOut.close()
