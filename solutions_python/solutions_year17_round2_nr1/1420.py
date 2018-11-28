INPUT_PATH = r"C:/Users/owner/Desktop/codejam16/2017B1/A-large.in"
OUTPUT_PATH = "A-answer.txt"

CASE = "CASE #%d: %f\n" 
answers = []

with open(INPUT_PATH, "r") as f:
    T = int(f.readline())
    for t in range(T):
        d, n = [int(x) for x in f.readline().split()]
        max_time = 0
        for i in range(n):
            ki, si = [int(x) for x in f.readline().split()]
            max_time = max(float(d-ki)/si, max_time)
        answers.append(d/max_time)
        
with open(OUTPUT_PATH, "w") as f:
    for i in range(len(answers)):
        f.write(CASE % (i+1, answers[i]))
