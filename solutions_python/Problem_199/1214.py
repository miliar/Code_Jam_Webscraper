
def read_file(filename: str):
    cases = []
    with open(filename) as f:
        T = int(f.readline().strip())
        for t in range(T):
            line = f.readline().split()
            K = int(line[1])
            S = list(line[0])
            cases.append({'K': K, 'S': S})
    return cases
