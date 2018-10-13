fin = open("small.in")
fout = open("ans.out", "w")

fin.readline()

for i, line in enumerate(fin):
    c, f, x = map(float, line.split())
    rate = 2.0
    won = False
    time = 0.0
    while won == False:
        time_to_win  = x / rate
        time_for_farm = c / rate
        new_rate = rate + f
        time_to_win_with_farm = x / new_rate + time_for_farm
        if time_to_win_with_farm < time_to_win:
            rate = new_rate
            time += time_for_farm
        else:
            time += time_to_win
            won = True
    fout.write("Case #" + str(i+1) + ": {0}".format(time) + "\n")
    print time

fin.close()
fout.close()
