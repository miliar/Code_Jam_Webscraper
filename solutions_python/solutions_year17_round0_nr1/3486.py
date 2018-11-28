def flip(s):
    return "-" if s == "+" else "+"

def flip_at(limit, x, s):
    if (limit + x) > len(s):
        return None
    else:
        return [s[i] if i < x or i >= x+limit else flip(s[i]) for i in range(len(s))]

def helper(s, limit, used):
    if len(s) < used:
        return -1
    if "-" not in s:
        # print (s, limit, used)
        return used
    i = s.index("-")
    s_copy = flip_at(limit, i, s)
    if s_copy:
    # print(i, s_copy)
        return helper(s_copy, limit, used+1)
    else:
        return -1

def solver(s, limit, used):
    result = helper(s, limit, used)
    if result == -1:
        return "IMPOSSIBLE"
    else:
        return result

results = []
contents = []

# solver("---+-++-", 3, 0)


with open("A-large.in") as f:
    contents = f.readlines()

total = int(contents[0])

for line in contents[1:]:
    content, limit = line.strip().split(" ")
    try:
        r = solver(content, int(limit), 0)
        results.append(r)
    except RuntimeError:
        print(content, limit)
        num = content.count("-")
        if num % 2 != 0:
            results.append("IMPOSSIBLE")
        else:
            indices = []
            result = 0
            for i in range(len(content)):
                if content[i] == "-":
                    indices.append(i)
            for i in range(len(indices)//2):
                result += (indices[i+1]-indices[i])
            results.append(result)

# print(results)

output_file = open('A-large.out', 'w')
output_str = ""
for r in range(len(results)):
    output_str += "Case #"
    output_str += str(r+1)
    output_str += ": "
    output_str += str(results[r])
    output_str += "\n"

output_file.write(output_str)
output_file.close()
