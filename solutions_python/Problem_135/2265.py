from sys import stdin

def find_card():
    card_row = int(stdin.readline())
    cards = []
    for rows in range(4):
        cards.append(list(map(int,stdin.readline().split())))
    return cards[card_row-1]

t = int(stdin.readline())
for kase in range(t):
    x = set(find_card())
    y = set(find_card())
    intersection = x.intersection(y)
    if len(intersection) == 1:
        print("Case #{}: {}".format(kase+1,intersection.pop()))
    elif len(intersection) == 0:
        print("Case #{}: {}".format(kase+1,"Volunteer cheated!"))
    else:
        print("Case #{}: {}".format(kase+1,"Bad magician!"))