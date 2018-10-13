filename = "tmp.txt"
file_out = "out.txt"

f = open(filename)
out = open(file_out,"w")

amount_tests = int(f.readline())

test = 0

while test < amount_tests:
    test += 1
    C,F,X = [float(j) for j in f.readline().split()]
    if X < C:
        print >> out, "Case #{}: ".format(test) + "{:.7f}".format(X/2.0)
    else:
        total_time = 0
        per_sec = 2.0

        time_without_fabric = X / per_sec
        total_time = time_without_fabric

        current_time = 0
        time_of_build_fibric = []
        while True:
            time_of_build_fibric.append( C/per_sec )
            per_sec += F
            time_with_fabric = X/per_sec
            current_time = sum(time_of_build_fibric) + time_with_fabric
            #print time_of_build_fibric, time_with_fabric, current_time, total_time

            if total_time < current_time:
                break
            total_time = current_time
        print >> out , "Case #{}: ".format(test) + "{:.7f}".format(total_time)

out.close()