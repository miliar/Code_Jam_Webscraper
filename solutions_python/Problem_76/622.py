def main():
    file = open(raw_input("Select file for processing: "))
    numcases = int(file.readline())
    for i in range(numcases):
        numcandies = int(file.readline())
        candies = map(int, file.readline().split(" "))
        seanpile = []
        patpile = []
        result = possible(candies, seanpile, patpile)
        if result > 0:
            print "Case #" + str(i + 1) + ": " + str(result)
        else:
            print "Case #" + str(i + 1) + ": NO"

def possible(candies, seanpile, patpile):
    if len(candies) == 0:
        if len(seanpile) == 0 or len(patpile) == 0:
            return -1
        seanval = reduce(lambda x, y: x ^ y, seanpile, 0)
        patval = reduce(lambda x, y: x ^ y, patpile, 0)
        if seanval == patval :
            return reduce(lambda x, y: x + y, seanpile, 0)
        else:
            return -1
    else:
        newcandies = list(candies)
        candy = newcandies.pop(0)
        if seanpile:
            newseanpile = list(seanpile)
            newseanpile.append(candy)
        else:
            newseanpile = [candy]
        if patpile:
            newpatpile = list(patpile)
            newpatpile.append(candy)
        else:
            newpatpile = [candy]
        tosean = possible(newcandies, newseanpile, patpile)
        topat = possible(newcandies, seanpile, newpatpile)
        if tosean == topat == -1:
            return -1
        elif tosean > topat:
            return tosean
        else:
            return topat
    

if __name__ == '__main__':
    main()
