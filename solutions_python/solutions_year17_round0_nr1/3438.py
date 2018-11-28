happyFace = "+"
blankFace = "-"
def isHappy(faces, flipper_size):
  
    if not blankFace in faces:
        return 0
    count = 0

    for idx, f in enumerate(faces):
        if f == blankFace:
            r = idx + flipper_size
            pancakeToFlip = faces[idx : r]
            if len(pancakeToFlip) < flipper_size:
                return "IMPOSSIBLE"
            faces[idx : r] = makeHappyFace(pancakeToFlip) 
            count = count + 1       

    if blankFace in faces:
        return "IMPOSSIBLE"
    else:
        return count


def makeHappyFace(pancakes):
    temp = []
    for p in pancakes:
        if p == blankFace:
            temp.append(happyFace)
        else:
            temp.append(blankFace)
    return temp


def main():

    print(isHappy(["-","-","-","+","-","+","+","-"], 3))
    print(isHappy(["+", "+", "+", "+", "+"], 4))
    print(isHappy(["-","+","-","+","-"], 4))




if __name__ == "__main__":
    with open("A-large.in", mode='r') as fp:
        testCase = int(fp.readline())
        count = 0
        for line in fp:
            data = line[:-1].split(" ")
            cakes = list(data[0])
            flipper = int(data[1])
            count = count + 1
            print("Case #{}: {}".format(count, isHappy(cakes, flipper)))