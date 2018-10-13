with open("B-large.in", "r") as inp:
    with open("B-large.out", "w") as outp:
        cases = int(inp.readline())
        for i in range(cases):
            num_list = [int(k) for k in inp.readline().strip()]
            if len(num_list) == 1:
                num_str = "".join([str(k) for k in num_list])
                outp.write("Case #" + str(i+1) + ": " + num_str + "\n")
                continue
            for j in range(1, len(num_list)):
                if num_list[j] < num_list[j-1]:
                    num_list[j-1] -= 1
                    for k in range(j, len(num_list)):
                        num_list[k] = 9
                    j -= 1
                    while j>0 and num_list[j] < num_list[j-1]:
                        num_list[j-1] -= 1
                        num_list[j] = 9
                        j -= 1
                    break
            if num_list[0] == 0:
                num_list = num_list[1:]
            num_str = "".join([str(k) for k in num_list])
            outp.write("Case #" + str(i+1) + ": " + num_str + "\n")
