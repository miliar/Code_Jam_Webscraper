__author__ = 'mehmetinan'

lines = open("A-small-attempt2.in").read().splitlines()

number = int(lines[0])
answers = []

a = 1
for i in range(0,int(number)):
    set = lines[a:a+10]
    answerset = []
    firstnumber = int(set[0])
    firstline = set[firstnumber].split()
    secondnumber = int(set[5])
    secondline = set[5+secondnumber].split()
    for number in firstline:
        if number in secondline:
            answerset.append(number)
    if len(answerset) == 1:
        answers.append(answerset[0])
    if len(answerset) > 1:
        answers.append('Bad magician!')
    if len(answerset) == 0:
        answers.append('Volunteer cheated!')
    a = a + 10

for i in range(0,len(answers)):
    print 'Case #%d:  %s' % (i+1,answers[i])