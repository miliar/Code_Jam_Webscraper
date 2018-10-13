def find_min_time(c, f, x):
    c = float(c)
    f = float(f)
    x = float(x)

    cookie_rate = 2
    t_elapsed = 0

    while True:
        # find out whether it is worth waiting for a other farm
        t_to_next_farm = c/cookie_rate

        t_wait = t_elapsed + x/cookie_rate
        t_with_farm = t_elapsed + t_to_next_farm + (x/(cookie_rate+f))

        if t_wait < t_with_farm:
            return t_wait
        else:
            t_elapsed += t_to_next_farm 
            cookie_rate += f

def main():
    _file = ""
    with open("B-large.in", "r") as inputfile:
        _file = inputfile.read()

    file_rows = _file.split("\n")
    file_rows = file_rows[1:]
    output = []

    for row in file_rows:
        data = row.split()
        if row:
            min_time = find_min_time(data[0], data[1], data[2])
            output.append(min_time)

    with open("output.txt", "w+") as outputfile:
        for i in range(len(output)):
            outputfile.write("Case #{0:}: {1:.7f}\n".format(i+1, output[i]))


if __name__ == "__main__":
    main()

