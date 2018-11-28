def main():
    with open("input.txt") as f:
        numberOfCases = int(next(f))
        
        for n in range(1, numberOfCases + 1):
            firstRow = int(next(f))
            firstRelevantCards = readRelevantCards(f, firstRow)
            secondRow = int(next(f))
            secondRelevantCards = readRelevantCards(f, secondRow)
            
            intersection = firstRelevantCards & secondRelevantCards
            
            if len(intersection) == 0:
                print("Case #" + str(n) + ": Volunteer cheated!")
            elif len(intersection) > 1:
                print("Case #" + str(n) + ": Bad magician!")
            else:
                print("Case #" + str(n) + ": " + list(intersection)[0])

def readRelevantCards(f, row):
    for i in range(row-1):
        next(f)
    
    relevantCards = set(next(f).split())
    
    for i in range(4-row):
        next(f)
        
    return relevantCards
     
main()