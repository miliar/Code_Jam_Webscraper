def change_pancake_face(face):
    if face == "+":
        return "-"
    elif face == "-":
        return "+"

def optimal_pancake_calculator(input_line):
    array_pancake = input_line.split(" ")
    pancakes = array_pancake[0]
    flipper = int(array_pancake[1])
    pancakes_array = [str(d) for d in str(pancakes)]
    length_pancakes_array = len(pancakes_array)
    j = 0
    while(j < length_pancakes_array):
        try:
            start_index = pancakes_array.index("-")
            end_index = pancakes_array.index("-") + flipper
        except ValueError:
            return j
        if end_index < length_pancakes_array+1:
            for i in range(start_index,end_index):
                pancakes_array[i] = change_pancake_face(pancakes_array[i])
        else:
            return "IMPOSSIBLE"
        j+=1

with open("/Users/smahimkar/Downloads/A-large.in", "r") as inp, open("/Users/smahimkar/Downloads/A-large.out", "w") as out:
    no_of_cases = int(inp.readline().strip())
    i=0
    for line in inp:
        i+=1
        input_line = line.strip()
        to_file = "Case #{}: {}\n".format(i, optimal_pancake_calculator(input_line))
        out.write(to_file)
