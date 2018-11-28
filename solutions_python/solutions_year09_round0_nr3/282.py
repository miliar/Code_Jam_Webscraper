target = "welcome to code jam"

def recurse(input_string, target_string) :
    if input_string == target_string :
        return 1

    if len(input_string) < len(target_string) :
        return 0

    if len(target_string) == 1 :
        return input_string.count(target_string)

    count = 0
    for i in range(input_string.count(target_string[0])) :
        input_string = input_string[input_string.index(target_string[0]) + 1:]
        count += recurse(input_string, target_string[1:])

    return count

with open('C-small-attempt0.in') as file :
    N = int(file.readline())
    for i in range(N) :
        input_string = file.readline().strip()
        print("Case #{}: {:04d}".format(i + 1, recurse(input_string, target) % 1000))
