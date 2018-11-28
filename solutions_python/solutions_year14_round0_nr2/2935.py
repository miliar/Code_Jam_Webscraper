def output_cases(cases):
    with open("output.txt", "w") as f:
        for i, ca in enumerate(cases):
            f.write("Case #{}: {}\n".format(i+1, ca))

def get_triple(line):
    return tuple(float(f) for f in line.strip().split(' '))

def solve(farm_cost, farm_production, target):
    production = 2
    time_elapsed = 0
    while True:
        time_to_target = target / production
        next_farm_cost = farm_cost / production
        next_step_cost = next_farm_cost + (target/(production+farm_production))
        if time_to_target < next_step_cost:
            return time_elapsed + time_to_target
        else:
            production += farm_production
            time_elapsed += next_farm_cost


def main():
    with open("input_2.txt", "r") as f:
        content = f.read()

    inputs = [get_triple(line) for line in content.strip().split('\n')[1:]]
    output_cases("%0.7f" % solve(*inp) for inp in inputs)
    

if __name__ == '__main__':
    main()
