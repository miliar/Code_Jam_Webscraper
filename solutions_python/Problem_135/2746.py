def parse_in():
    lines = open('/home/toon/Downloads/A-small-attempt2.in').readlines()
    for a in range(len(lines))[1::10]:
        ans1 = int(lines[a])
        r1 = []
        for x in range(1,5):
            r1.append(map(int,lines[a + x].split()))
        ans2 = int(lines[a + 5])
        r2 = []
        for x in range(6,10):
            r2.append(map(int,lines[a + x].split()))
        yield (ans1,ans2,r1,r2)
        

def answer(a1,a2,r1,r2):
    print(a1,a2,r1,r2)
    answers = []
    for x in range(1,17):
        print(x)
        if x in r1[a1-1] and x in r2[a2-1]:
            print("in")
            answers.append(x)
    if not answers:
        return "Volunteer cheated!"
    elif len(answers) == 1:
        return answers[0]
    elif len(answers) > 1:
        return "Bad magician!"

caseno = 1
outf = open('/home/toon/Code/codejam/ans.out','w')
def out(s):
    global caseno
    outf.write("Case #{}: {}\n".format(caseno,s))
    caseno += 1

if __name__ == "__main__":
    for a1,a2,r1,r2 in parse_in():
        a = answer(a1,a2,r1,r2)
        print(a)
        out(a)

