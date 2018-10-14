__author__ = 'ceciet'


def magic_trick():

    with open('file/A-small-attempt2.in') as input_file, open('file/A-small-attempt2.out', 'w') as output_file:
        testNum = input_file.readline().strip()
        for i in range(0, int(testNum)):
            print i
            firstPos = input_file.readline().strip()
            print firstPos
            firstPos = int(firstPos)
            firstOrder = []
            for j in range(0, 4):
                orders = input_file.readline().strip()
                orders = orders.split()
                orders = [int(order) for order in orders]
                #print orders
                firstOrder.append(orders)
            print firstOrder
            secondPos = int(input_file.readline().strip())
            secodeOrder = []
            for j in range(0, 4):
                orders = input_file.readline().strip()
                orders = orders.split()
                orders = [int(order) for order in orders]
                #print orders
                secodeOrder.append(orders)
            #print secodeOrder
            #list(set(a).intersection(set(b)))
            result = list(set(firstOrder[firstPos-1]).intersection(set(secodeOrder[secondPos-1])))
            #print result
            if len(result) == 0:
                resultLine = "Case #" + str(i+1) + ": Volunteer cheated!\n"
            elif len(result) > 1:
                resultLine = "Case #" + str(i+1) + ": Bad magician!\n"
            elif len(result) == 1:
                resultLine = "Case #" + str(i+1) + ": " +str(result[0]) + '\n'
            output_file.write(resultLine)



if __name__ == '__main__':

    magic_trick()