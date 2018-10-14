file = open('A-small-attempt0.in','r')
fileans = open('ansA.txt','w')

case_num = int(file.readline().replace('\n', ''))
for i in range(case_num):
    ans = ''
    deck_1 = []
    deck_2 = []
    guess_1 = int(file.readline().replace('\n', ''))
    for x in range(4):
        deck_1.append(file.readline().replace('\n', '').split())
    guess_2 = int(file.readline().replace('\n', ''))
    for x in range(4):
        deck_2.append(file.readline().replace('\n', '').split())
    
    m = set(deck_1[guess_1-1])
    y = set(deck_2[guess_2-1])
    
    ans = m.intersection(y)
    if (len(ans)>1):
        ans = "Bad magician!"
    elif(len(ans)<1):
        ans =  "Volunteer cheated!"
    else:
        ans = list(ans)[0]
    if (deck_1 == deck_2):
        if (guess_1 == guess_2):
            ans = "Bad magician!"
        else:
            ans =  "Volunteer cheated!"
    fileans.write("Case #%s: %s\n" % (i+1,ans))
file.close()
fileans.close()
print('DONE')