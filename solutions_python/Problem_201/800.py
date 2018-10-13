import heapq

file_input = open("stalls-large.in","r") 
file = open("stalls.out", "w+") 

num_cases = int(file_input.readline().rstrip())

for case in range(num_cases):
    line = file_input.readline().rstrip()
    
    stalls, people = [int(s) for s in line.split(" ")]

    first_obj = -stalls
    heap = [first_obj]

    max_num = 0
    min_num = 0

    gaps = {
        stalls: 1
    }

    while people > 0:
        size = max(k for k, v in gaps.iteritems())

        num_gaps = gaps.pop(size, None)

        people -= num_gaps

        num_left = size - 1

        if num_left % 2 == 0:
            new_gap_size = num_left / 2
            new_num_gaps = num_gaps * 2

            if new_gap_size in gaps:
                gaps[new_gap_size] += new_num_gaps
            else:
                gaps[new_gap_size] = new_num_gaps

            max_num = new_gap_size
            min_num = new_gap_size
        else:
            new_large_gap_size = num_left / 2 + 1
            new_num_gaps = num_gaps

            if new_large_gap_size in gaps:
                gaps[new_large_gap_size] += new_num_gaps
            else:
                gaps[new_large_gap_size] = new_num_gaps

            new_small_gap_size = num_left / 2

            if new_small_gap_size in gaps:
                gaps[new_small_gap_size] += new_num_gaps
            else:
                gaps[new_small_gap_size] = new_num_gaps

            max_num = new_large_gap_size
            min_num = new_small_gap_size

    # for person in range(people):
    #     gap = heapq.heappop(heap)

    #     gap = -gap

    #     if case == 5:
    #         print gap

    #     remaining = gap - 1

    #     min_num = remaining / 2
    #     max_num = remaining / 2 if remaining % 2 == 0 else remaining / 2 + 1

    #     if min_num > 0:
    #         heapq.heappush(heap, -min_num)

    #     if max_num > 0:
    #         heapq.heappush(heap, -max_num)

    file.write("Case #" + str(case + 1) + ": " + str(max_num) + " " + str(min_num) + "\n")

file_input.close()
file.close()