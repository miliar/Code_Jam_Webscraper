def crowd_standing(crowd, guests):
    total = guests
    i = 0
    while i <= total and i < len(crowd):
        total += crowd[i]
        i += 1
    return total - guests

def needed_guests(crowd):
    total_crowd = sum(crowd)
    guests = 0
    while crowd_standing(crowd, guests) < total_crowd:
        guests += 1
    return guests

def parse_line(line):
    max_shy_s, crowd_s = line.split()
    max_shy = int(max_shy_s)
    crowd = map(int, list(crowd_s))
    return max_shy, list(crowd)

tests = int(input())
for i in range(tests):
    _, crowd = parse_line(input())
    guests = needed_guests(crowd)
    print("Case #{}: {}".format(i + 1, guests))