fname = "A-large.in"

with open(fname) as f:
    content = f.readlines()

content = [x.strip() for x in content]


line_counter = 0

for test_case_i in range(0, int(content[0])):
    line_counter += 1
    # print("\n\n### case: " + str(i))
    n_horses = int(content[line_counter].split(' ')[1])
    dest = int(content[line_counter].split(' ')[0])
    # print("Anniee wants to go to " + str(dest))
    # print("n_horses: " + str(n_horses))

    list_of_horses = []
    for j_horse in range(0, n_horses):
        line_counter += 1
        horse_values = content[line_counter].split(' ')
        horse_start = int(horse_values[0])
        horse_speed = int(horse_values[1])
        list_of_horses.append({'start': horse_start,
                               'speed': horse_speed})

    sorted_list_of_horses = sorted(list_of_horses, key=lambda x: x['start'], reverse=True)
    # print(sorted_list_of_horses)

    horse0 = list_of_horses[0]
    # print("Horse " + str(j) + " with " + str(horse0))
    time = (int(dest) - int(horse0['start'])) / int(horse0['speed'])
    # print("(Without interruption) horse will reach dest at " + str(time))
    last_max_time = time

    for k in range(1, len(list_of_horses)):
        current_horse = list_of_horses[k]
        # print("Horse " + str(j) + " with " + str(current_horse))
        # if (current_horse['speed'] > list_of_horses[k - 1]['speed']):
        #     pass
        # else:
        time = (int(dest) - int(current_horse['start'])) / int(current_horse['speed'])
        # print("The horse is slower than the one before it, will reach dest after " + str(time))
        if time > last_max_time:
            last_max_time = time

    annies_time = dest / last_max_time

    print("Case #" + str(test_case_i + 1) + ": %0.6f" % round(annies_time, 6))
