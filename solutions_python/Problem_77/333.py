lines = open("D-large.in", "r").readlines()
out_file = open("D-large.out", "w")
for i, line in enumerate(lines[1:]):
	if i%2 == 1:
		out_file.write("Case #" + str((i+1)/2) + ": " + str(goran_sort(line)) + "\n")
out_file.close()

def goran_sort(line):
    elements = [int(element) for element in line.split()]
    count = len(elements)
    # binary sort, how many steps?
    # sort the array, find how many are not in the right place
    sorted_elements = list(elements)
    sorted_elements.sort()
    num_out_of_order = 0
    for i, element in enumerate(sorted_elements):
        if elements[i] != element:
            num_out_of_order += 1
    # return the count of ones out of place as the answer
    return num_out_of_order
