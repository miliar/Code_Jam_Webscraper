t = int(raw_input())
f = open('out', 'w')

for i in xrange(1, t + 1):
    stall_num, people_num = map(int, raw_input().split(" "))
    room = "o" + ("." * stall_num) + "o"

    for l in range(people_num):
        empty_max = 0
        empty_counter = 0

        poss_index = None

        for j in range(len(room)):
            if room[j] == "o":
                if empty_counter > 0:
                    if empty_counter > empty_max:
                        poss_index = j - (empty_counter / 2) - 1
                        empty_max = empty_counter

                if j != len(room) - 1:
                    empty_counter = 0
            else:
                empty_counter += 1

        room = room[:poss_index] + "o" + room[poss_index + 1:]

        if l == people_num - 1:
            if empty_max % 2 == 1:
                f.write("Case #{}: {} {}\n".format(i, (empty_max - 1) / 2, (empty_max - 1) / 2))
            else:
                f.write("Case #{}: {} {}\n".format(i, empty_max / 2, (empty_max / 2) - 1))

f.close()
