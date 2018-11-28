from solver import solver


@solver(lines_per_case="args[1]")
def cruise(lines):
    d = int(lines[0].split()[0])
    hs = [tuple(map(int, line.split()))
          for line in lines[1:]]
    t = max((d-a)/b for a, b in hs)
    return d/t

if __name__ == "__main__":
    cruise.from_cli()
