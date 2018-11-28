__author__ = 'ashwin'


def solve(aud):
    so = 0
    answer = 0
    for s,p in enumerate(aud):
        if not p: continue
        new = max(s-so, 0)
        answer += new
        so += new
        so += p
    return answer


def run(infilepath, outfilepath):
    with open(infilepath) as infile, open(outfilepath, 'w') as outfile:
        infile.readline()
        for t, line in enumerate(infile, 1):
            aud = line.split(None, 1)[1].rstrip()
            aud = [int(i) for i in aud]
            outfile.write("Case #{}: {}\n".format(t, solve(aud)))


if __name__ == "__main__":
    print('starting')
    run('A-large.in', 'A-large.out')
    print('done')