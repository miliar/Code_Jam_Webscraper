text = open('A-large.in')
test_cases = int(text.readline())


for i in range(test_cases):
    case = text.readline()
    l = case.split(' ')
    count = 0
    friends = 0
    for j in range(int(l[0])):
        count = count + int(l[1][j])
        if count<j+1:
            friends = friends + (j+1-count)
            count = j+1
    print("Case #"+str(i+1)+": "+str(friends))
