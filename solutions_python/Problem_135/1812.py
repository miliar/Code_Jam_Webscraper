from codejam import readfile, takeby

problems = list(takeby((1+4)*2, readfile()[1:]))
for index,problem in enumerate(problems,1):
    first, second = problem[:5], problem[5:]
    row1 = set(first[1:][int(first[0])-1].split())
    row2 = set(second[1:][int(second[0])-1].split())
    answer = row1.intersection(row2)
    print "Case #%s:" % index,
    if len(answer) > 1:
        print "Bad magician!"
    elif len(answer) == 0:
        print "Volunteer cheated!"
    else:
        print list(answer)[0]
