# Google Code Jam 2017
# Qualification Round
# Problem B. Tidy Numbers

def is_tidy(N): return N == int(''.join(sorted(str(N))))

def last_tidy_num(N):
    if is_tidy(N):
        return N
    else:
        num_digits = len(str(N))
        for i in range(num_digits):
            if not is_tidy(int(str(N)[:i+1])):
                break
        return last_tidy_num(int(str(int(str(N)[:i]) - 1) + '9'*len(str(N)[i:])))

t = int(input())  # read a line with a single integer
for case in range(1, t + 1):
    N = int(input())
    print("Case #{0}: {1}".format(case, last_tidy_num(N)))

# --- HOW TO USE ---
# python test.py < input > output