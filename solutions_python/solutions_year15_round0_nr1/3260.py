def one_line_solver(shynesses):
    shynesses = map(int, shynesses)
    invited, standed = 0, 0
    for shyness, people in enumerate(shynesses):
        while (shyness) > (standed + invited):
            invited += 1
        standed += people
    return invited


def solver():
    with open("./A-large.in", "r") as f:
        input_string = f.read()
    cases = input_string.splitlines()[1:]
    for i, case in enumerate(cases):
        with open("output-large.txt", "a") as f:
            f.write("Case #{}: {}\n".format(i+1, one_line_solver(case.split(" ")[1])))
