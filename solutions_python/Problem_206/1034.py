import os

input_file = open("input_large.in", "r")
output_file = open("output_large.out", "w")

cases = int(input_file.readline())

for i in range(cases):
    params = input_file.readline().split(" ")
    full_dist = float(params[0])
    num_horses = int(params[1])

    h_distances = []
    h_speeds = []

    for h in range(num_horses):
        h_params = input_file.readline().split(" ")
        h_start_pos = int(h_params[0])
        h_speed = int(h_params[1])

        h_distances.append(float(full_dist) - float(h_start_pos))
        h_speeds.append(float(h_speed))

    time_remaining = [h_distances[j] / h_speeds[j] for j in range(len(h_distances))]
    annie_time = max(time_remaining)
    annie_speed = full_dist / annie_time

    output_file.write("Case #" + str(i + 1) + ": " + str(annie_speed) + "\n")






