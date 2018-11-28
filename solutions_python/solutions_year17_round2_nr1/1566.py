def horses():
    user_info = input("")
    space_position = user_info.find(" ")
    user_position = ""
    for i in range(space_position):
        user_position += user_info[i]

    inte_user_position = int(user_position)
    other_horses = ""
    for i in range(space_position +1, len(user_info)):
        other_horses += user_info[i]
    inte_other_horses = int(other_horses)
    fake_horse_loc = []
    fake_horse_sped = []
    for i in range(1,inte_other_horses+1):
        fake_horse_info = input("")
        fake_space = fake_horse_info.find(" ")
        horse_loc = fake_horse_info[0:fake_space]
        fake_horse_loc.append(int(horse_loc))
        horse_sped = fake_horse_info[fake_space +1: len(fake_horse_info)]
        fake_horse_sped.append(int(horse_sped))

    rev_fake_horse_loc = fake_horse_loc.reverse()
    rev_fake_horse_sped = fake_horse_sped.reverse()
    max_time = 0
    for i in range(len(fake_horse_loc)):
        time = (inte_user_position - fake_horse_loc[i]) / fake_horse_sped[i]
        if time > max_time:
            max_time = time
    return inte_user_position / max_time

test = int(input(""))
for i in range(1, test+1):
    print("Case #" + str(i) + ": "+ str(horses()))
