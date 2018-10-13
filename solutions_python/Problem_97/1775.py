def find_wins(line):
    line_list = line.split()
    A = int(line_list[0])
    B = int(line_list[1])
    total_wins = 0
    done = []
    current = B
    while current >= A:
        more_wins, done = check_possible(current, A, B, done)
        total_wins += more_wins
        current -= 1
    return total_wins
        
def check_possible(current, A, B, done):
    string_cur = str(current)
    win = 0
    possible_count = len(string_cur) - 1
    
    while possible_count:
        recycled_number = int(string_cur[possible_count:] + string_cur[0:possible_count])
        if recycled_number < current and recycled_number >= A and (current, recycled_number) not in done:
            win += 1
            done.append((current, recycled_number))
        possible_count -= 1
    return (win, done)


pagename = "C-small-attempt.in"
page = open(pagename, "r")
number_of_tests = int(page.readline().strip())
answer_pagename = "C-small-answers.in"
answer_page = open(answer_pagename, "w")
for i in range(1, number_of_tests + 1):
    line = page.readline()
    answer_page.write("Case #%d: %d\n" % (i, find_wins(line) ))
answer_page.close()