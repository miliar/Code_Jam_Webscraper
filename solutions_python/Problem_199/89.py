def is_pancakes_happy(pancakes, flip_size):
    temp_bool_list = []
    for p in pancakes:
        temp_bool_list.append(p == "+")

    counter = 0
    for i in range(len(temp_bool_list) - flip_size + 1):
        if not temp_bool_list[i]:
            for j in range(flip_size):
                temp_bool_list[i + j] = not temp_bool_list[i + j]
            counter += 1

    for i in range(len(temp_bool_list) - flip_size + 1, len(temp_bool_list)):
        if not temp_bool_list[i]:
            return "IMPOSSIBLE"

    return counter

def phase_input():
    pancakes, flip_size = input().split(" ")
    flip_size = int(flip_size)
    return pancakes, flip_size

def main():
    test_times = int(input())
    for t in range(test_times):
        P, F = phase_input()
        print("Case #%d: %s" %(t + 1, is_pancakes_happy(P, F)))
    
if __name__ == '__main__':
    main()