def read_input(path):
    with open(path) as f:
        lines = f.read().split("\n")[1:]

    out = []
    for line in lines:
        if len(line.split(" ")) > 1:
            out.append({
                "max_shy": int(line.split(" ")[0]),
                "shyness": map(int, line.split(" ")[1])
            })


    return out


output = ""
path = "A-large.in"
for i, data in enumerate(read_input(path)):
    # No need to add any if there is nobody there
    if len(data["shyness"]) <= 1:
        output += "Case #{}: {}\n".format(i+1, 0)
        continue

    standing = data["shyness"][0]
    friends = 0
    required = 0
    for people in data["shyness"][1:]:
        required += 1

        if standing < required and people > 0:
            friends += required - standing
            standing += required - standing

        standing += people

    output += "Case #{}: {}\n".format(i+1, friends)

# Remove the last linebreak
output = output[:-1]
with open(path.replace(".in", ".out"), "w") as f:
    f.write(output)