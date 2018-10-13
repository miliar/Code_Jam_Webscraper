fname = "B-large.in"
with open(fname) as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]

def tidy_number(num):
    last_digit = str(num)[0]
    # pos = len(str(num)) - 2
    # for ch in str(num)[1:]:
    #     if ch < last_digit:
    #         return pos
    #     else:
    #         pos -= 1
    #         last_digit = ch
    pos = 0
    for i in range(1, len(str(num))):
        if str(num)[-i-1] > str(num)[-i]:
            return pos
        else:
            pos += 1
    return -1

id = 1
for line in content[1:]:
    found = False
    i = int(line)
    while not found:
        return_val = tidy_number(i)
        if return_val == -1:
            s = 'Case #' + str(id) + ': '
            print(s + str(i))
            id += 1
            found = True
        else:
            if i % (10**return_val) == 0:
                i -= 1
            else:
                i -= i % (10**return_val)

