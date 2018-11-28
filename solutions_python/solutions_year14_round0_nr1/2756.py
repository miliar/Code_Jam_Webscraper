
def main(deck1, row1, deck2, row2):
   cards = set(deck1[row1-1]) & set(deck2[row2-1])
   return cards

def read_deck():
    return [[int(x) for x in input().split()] for _ in range(4)]

n_cases = int(input())
for n in range(n_cases):
    row1 = int(input())
    deck1 = read_deck()
    row2 = int(input())
    deck2 = read_deck()
    result = main(deck1, row1, deck2, row2)
    if len(result) == 1:
        print("Case #{}: {}".format(n+1, result.pop()))
    elif len(result) == 0:
        print("Case #{}: Volunteer cheated!".format(n+1))
    else:
        print("Case #{}: Bad magician!".format(n+1))
