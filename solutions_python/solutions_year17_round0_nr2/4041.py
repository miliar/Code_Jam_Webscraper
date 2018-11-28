def is_tidy(num):
    if num < 10:
        return True
    digits = [int(c) for c in str(num)]
    if 0 in digits:
        return False
    for i in range(len(digits)-1):
        if digits[i+1] < digits[i]:
            return False
    return True

# tidy_numbers = []

# for i in range(1, 1000):
    # if is_tidy(i):
        # tidy_numbers.append(i)

def solver(N):
    for n in range(N, 0, -1):
        if is_tidy(n):
            return n

results = []
contents = []


with open("B-small-attempt0.in") as f:
    contents = f.readlines()

total = int(contents[0])

for line in contents[1:]:
    content = int(line.strip())
    try:
        r = solver(content)
        results.append(r)
    except RuntimeError:
        print(content)

# print(results)

output_file = open('B-small-attempt0.out', 'w')
output_str = ""
for r in range(len(results)):
    output_str += "Case #"
    output_str += str(r+1)
    output_str += ": "
    output_str += str(results[r])
    output_str += "\n"

output_file.write(output_str)
output_file.close()
