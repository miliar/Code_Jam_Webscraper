import sys
import string

try:
    f = open(sys.argv[1], 'r')
except:
    print "Specify input file"
    sys.exit()

# Don't care about recording the number of cases.
current_line = f.readline()

# Vars
out = ''

in_text = f.readlines()
# For each use case..
for i in range(len(in_text)):
    current_line = in_text[i]
    out = ''.join((out, "Case #", str(i + 1), ": "))

    c_line_vals = str.split(current_line)
    c_line_vals.pop(0)  # number of dancers
    surprises = int(c_line_vals.pop(0))
    score_to_match = int(c_line_vals.pop(0))
    best_results = 0
    scores = c_line_vals

    # For each contestant/dancer score..
    for j in range(len(scores)):

        nums = [score_to_match, score_to_match, score_to_match]
        remaining = int(scores[j]) - (score_to_match * 3)

        # We can have something like p = 5, score >= 15.
        if remaining >= 0:
            best_results = best_results + 1
            continue
        
        # Need to check that we can sub 1 from two scores, and that we
        # have enough value remaining: p = 7, score = 7 + 6 + 6.
        # Can't have negatives.
        
        gr = 0

        for k in range(len(nums)):
            if nums[k] > 1:
                gr = gr + 1

        if gr >= 2 and remaining >= -2:
            best_results = best_results + 1
            continue

        # Same case as above but now we need to use surprise.

        gr = 0

        for k in range(len(nums)):
            if nums[k] > 2:
                gr = gr + 1

        if gr >= 2 and remaining >= -4 and surprises > 0:
            best_results = best_results + 1
            surprises = surprises - 1

    out = ''.join((out, str(best_results), "\n"))

print out
