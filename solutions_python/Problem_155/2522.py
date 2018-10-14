def read_cases(filepath):
    cases = []
    with open(filepath, 'r') as f:
        for i in range(int(f.readline())):
            s, p = f.readline().split(' ')
            cases.append((int(s), map(int, p.strip())))
    return cases


def calculate_invitations(cases):
    invited = []
    for case_idx, case in enumerate(cases):
        standing = 0
        need = 0
        for idx, people in enumerate(case[1]):
            if standing < idx:
                d = idx - standing
                need += d
                standing += d
            standing += people
        invited.append(need)
    return invited

if __name__ == "__main__":
    cases = read_cases('./A-large.in')
    invited = calculate_invitations(cases)

    msg = "Case #%d: %d"
    with open('./ovation.out', 'w+') as out:
        out.write('\n'.join([msg % (i + 1, p) for i, p in enumerate(invited)]))
