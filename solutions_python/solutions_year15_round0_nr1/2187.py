def get_next_num(file):
    num = ""
    while True:
        char = file.read(1)
        if char == " " or char == "\n" or char == "": break
        num += char
    num = int(num)
    return num

def str_to_list(file):
    ans = []
    while True:
        char = file.read(1)
        if char == " " or char == "\n" or char == "": break
        ans.append(int(char))
    return ans

def run():
    print("Filename:")
    in_file = open(input())
    out_file = open("output.txt", "w")

    num_cases = int(in_file.readline()[:-1])

    for case in range(1, num_cases + 1):

        s_max = get_next_num(in_file)
        s_list = str_to_list(in_file)

        num_standing = 0
        required = 0
        for s_level in range(len(s_list)):
            while s_level > num_standing:
                num_standing += 1
                required += 1
            num_standing += s_list[s_level]

        out_file.write("Case #" + str(case) + ": " + str(required) + "\n")

run()
