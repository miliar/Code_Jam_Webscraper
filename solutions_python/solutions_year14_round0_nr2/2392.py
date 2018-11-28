if __name__ == "__main__":

    with open("sample.txt", "r") as f:
        test_c = int(f.readline())

        for t in range(1, test_c + 1):

            C, F, X = [float(v) for v in f.readline().split(" ")]

            current_speed = 2.0
            current_time_to_win = X/current_speed
            spended_time_on_farms = 0
            farm_c = 0
            current_time_to_next_farm = C/current_speed

            while  spended_time_on_farms + current_time_to_next_farm + (X / (current_speed + F)) < current_time_to_win:
                current_time_to_win = spended_time_on_farms + current_time_to_next_farm + (X / (current_speed + F))
                current_speed += F
                spended_time_on_farms += current_time_to_next_farm
                current_time_to_next_farm = C/current_speed  
                farm_c += 1

            print "Case #" + str(t) + ": " + str(round(current_time_to_win,7))