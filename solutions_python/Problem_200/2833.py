INPUT_PATH = r"C:/Users/owner/Desktop/codejam16/2017qual/B-large.in"
OUTPUT_PATH = "answer.txt"

CASE = "Case #%d: %d\n"

answers = []
with open(INPUT_PATH, "r") as f:
    for t in range(int(f.readline())):
        x = f.readline()
        if x[-1] == "\n":
            x = x[:-1]
        while True:
            #print(x)
            for i in range(1, len(x)):
                if int(x[i-1]) > int(x[i]):
                    break
            else:
                answers.append(int(x))
                break
            x = int(x[:i]) * (10 **(len(x)-i))
            x -= 1
            x = str(x)

with open(OUTPUT_PATH, "w") as f:
    for i in range(len(answers)):
        print(CASE % (i+1, answers[i]))
        f.write(CASE % (i+1, answers[i]))
