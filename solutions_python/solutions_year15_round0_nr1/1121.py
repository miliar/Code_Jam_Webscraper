
f = open("A-large.in", 'r')
out = open("Answer.txt", "w")
case = 0
for line in f:
    num_people = 0
    num_extra = 0
    shy_level = 0
    fields = line.split(" ")
    if len(fields) == 1:
        continue
    case += 1
    max_shy = int(fields[0])
    stats = fields[1]
    for c in stats:
        if not c.isdigit():
            break
        if num_people < shy_level:
            num_people += 1
            num_extra += 1
        shy_level += 1
        num_people += int(c)
    output = "Case #" + str(case) + ": " + str(num_extra) + "\n"
    out.write(output)
        
f.close()
out.close()
