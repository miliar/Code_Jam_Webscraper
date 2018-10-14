def man_choice(now_box, now_toy, box_line, toy_line, boxed_toys=0):
    if now_box == [] or now_box[0] == 0:
        if len(box_line) == 0:
            now_box = []
        else:
            now_box = box_line[:2]
        box_line = box_line[2:]
    if now_toy == [] or now_toy[0] == 0:
        if len(toy_line) == 0:
            now_toy = []
        else:
            now_toy = toy_line[:2]
            toy_line = toy_line[2:]

    if now_box == [] or now_toy == []:
        return boxed_toys
    
    if now_toy[1] == now_box[1]:
        complete = min(now_box[0], now_toy[0])
        now_toy[0] -= complete
        now_box[0] -= complete
        return man_choice(now_box, now_toy, box_line, toy_line, boxed_toys+complete)
    else:
        choice0 = man_choice(box_line[:2], now_toy, box_line[2:], toy_line, boxed_toys)
        choice1 = man_choice(now_box, toy_line[:2], box_line, toy_line[2:], boxed_toys)
        return max(choice0, choice1)

outfile = open("results.txt", "w")

file_data = open("C-small-attempt0.in")
tests = int(file_data.readline())
for test in xrange(tests):
    file_data.readline()
    boxes = file_data.readline().split()
    boxes = map(int, boxes)
    toys = file_data.readline().split()
    toys = map(int, toys)
    results = man_choice([], [], boxes, toys)
    outfile.write("Case #%d: %d\n" %(test+1, results))

outfile.close()
print "finish"
