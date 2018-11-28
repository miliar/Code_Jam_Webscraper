f = open('A-large.in', 'r')
g = open('A-large.out', 'w')
# f = open('A-small-attempt1.in', 'r')
# g = open('A-small-attempt1.out', 'w')
t = int(f.readline())

for i in xrange(t):
    s_max, s_list = (f.readline().replace('\n','').split(' '))
    s_list = [int(c) for c in s_list]

    num_friends = 0
    standing_people = 0
    for s, people in enumerate(s_list):
        if standing_people + num_friends < s and people > 0:
            num_friends += s - standing_people - num_friends
        standing_people += people
    g.write("Case #"+str(i+1)+": "+str(num_friends)+"\n")