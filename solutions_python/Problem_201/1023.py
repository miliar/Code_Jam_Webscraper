def max_min(num):
    return (num // 2, (num-1) // 2)

def solve(num):
    n, k = (int(a) for a in line.split())
    
    runs = {n: 1}
    
    max_run = max(runs.keys())
    while k > runs[max_run]:
        k -= runs[max_run]
        new_runs = max_min(max_run)
        runs[new_runs[0]] = runs.get(new_runs[0], 0) + runs[max_run]
        runs[new_runs[1]] = runs.get(new_runs[1], 0) + runs[max_run]
        del runs[max_run]
        max_run = max(runs.keys())
        
    return max_min(max(runs.keys()))
   

with open("C-large.in") as f:
    i = 1
    with open("C-large.out", "w") as w:
        f.readline()
        for line in f:
            answer = solve(line.strip())
            print("Case #{0}: {1} {2}".format(i, answer[0], answer[1]))
            w.write("Case #{0}: {1} {2}\n".format(i, answer[0], answer[1]))
            i += 1