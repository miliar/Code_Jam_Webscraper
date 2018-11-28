def main():
    f = open("A-small-attempt0.in", "r")
    cases = int(f.readline())
    for i in range(1,cases+1):
        cards = {}

        line = int(f.readline())
        for j in range(1,5):
            if j == line:
                cards = set(f.readline().split())
            else: 
                f.readline()
        line = int(f.readline())
        for j in range(1,5):
            if j == line:
                cards = cards.intersection(set(f.readline().split()))
            else: 
                f.readline()
        
        if len(cards) == 0:
            print("Case #" + str(i) + ": Volunteer cheated!")
        elif len(cards) == 1:
            print("Case #" + str(i) + ": " + str(cards.pop()))
        else:
            print("Case #" + str(i) + ": Bad magician!")

if __name__ == "__main__":
    main()