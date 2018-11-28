f = open('Google Magic Trick Small.in','r')
g = open('Google Magic Trick Small.out','w')
def find_card(a1,a2,r1,r2):
    cards = [x for x in a1[r1-1] if x in a2[r2-1]]
    if len(cards) == 0:
        return 'Volunteer cheated!'
    if len(cards) == 1:
        return str(cards[0])
    if len(cards) > 1:
        return 'Bad magician!'


def Google_print(filename,answers):
    for i in range(len(answers)):
        filename.write("Case #%s: %s\n" % (str(i+1),answers[i]))
        print "Case #%s: %s" % (str(i+1),answers[i])
    return

cases = int(f.readline())
answers = []
for i in range(cases):
    r1 = int(f.readline())
    a1 = []
    for j in range(4):
        row = f.readline().rstrip().split(' ')
        a1.append(row)
    r2 = int(f.readline())
    a2 = []
    for j in range(4):
        row = f.readline().rstrip().split(' ')
        a2.append(row)
    answers.append(find_card(a1,a2,r1,r2))

Google_print(g,answers)
f.close()
g.close()

