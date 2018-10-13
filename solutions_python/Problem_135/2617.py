
sample_input = """3
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
3
1 2 5 4
3 11 6 15
9 10 7 12
13 14 8 16
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
3
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16""";

import cStringIO;


#f_in = cStringIO.StringIO(sample_input);
f_in = open("A-small-attempt0.in", "r");
f_iter = iter(f_in);

T = int(f_iter.next().strip());

for t in range(T):
    answer1 = int(f_iter.next().strip())-1;
    
    cards1 = [];
    for row in range(4):
        cards_row = map(int, f_iter.next().strip().split(" "));
        cards1.append(cards_row);
    
    answer2 = int(f_iter.next().strip())-1;
    cards2 = [];
    for row in range(4):
        cards_row = map(int, f_iter.next().strip().split(" "));
        cards2.append(cards_row);    
    
    possibilities = [];
    for card in cards1[answer1]:
        if card in cards2[answer2]:
            possibilities.append(card);
    
    print "Case #%i:" % (t+1),;
    if len(possibilities) == 1:
        print possibilities[0];
    elif len(possibilities) > 1:
        print "Bad magician!";
    else:
        print "Volunteer cheated!";
    
