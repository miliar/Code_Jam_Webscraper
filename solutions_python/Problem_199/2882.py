#problem 1 solution

def get_input():
    input_array = []
    with open("A-large.in", "r") as ins:
        cases = int(ins.readline())
        for line in ins:
            split_line = line.split(" ")
            cookies = split_line[0]
            flipper_size = int(split_line[1])
            input_array.append({"cookies":cookies, "flipper_size":flipper_size})
    return input_array

def solve(problem):
    """
    solve a problem set
    """
    dummy_side = '*'
    happy_side = '+'
    bad_side = '-'
    cookies = problem['cookies']
    number_of_cookies = len(cookies)
    flipper_size = problem['flipper_size']
    tries = 0
    while (True):
        if not bad_side in cookies:
            break
        if number_of_cookies - cookies.index(bad_side)<flipper_size:
            return "IMPOSSIBLE"
        cookies_before = cookies[:cookies.index(bad_side)]
        cookies_to_flip = cookies[cookies.index(bad_side):cookies.index(bad_side)+flipper_size]
        cookies_after = cookies[cookies.index(bad_side)+flipper_size:]
        cookies_to_flip = cookies_to_flip.replace(happy_side, dummy_side)
        cookies_to_flip = cookies_to_flip.replace(bad_side, happy_side)
        cookies_to_flip = cookies_to_flip.replace(dummy_side, bad_side)
        cookies = cookies_before + cookies_to_flip + cookies_after
        tries+=1
    return tries


def solution():
    output_string = """"""
    inputs = get_input()
    for count, problem in enumerate(inputs):
        output_string+="Case #{}: {}\n".format(count+1, solve(problem))
    output_file = open('output_problem1.txt', 'w+')
    output_file.write(output_string)


if __name__ == "__main__":
    solution()