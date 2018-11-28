import sys

#From http://www.saltycrane.com/blog/2007/11/python-circular-buffer/
class RingBuffer:
    def __init__(self, size):
        self.data = [None for i in xrange(size)]

    def append(self, x):
        self.data.pop(0)
        self.data.append(x)

    def get(self):
        return self.data

    def pop(self):
        item = self.data.pop(0)
        self.data.append(item)
        return item

    def push(self):
        item = self.data.pop(len(self.data) - 1)
        self.data.insert(0, item)
        return item


def main() :
    if (len(sys.argv) != 2) :
        print sys.argv[0] + " [input file]"
        return

    input = open(sys.argv[1])

    limit = int(input.readline())
    print "Handling " + str(limit) + " cases."

    output = open("output.txt", "w")


    for ii in xrange(0, limit, 1) :
        line = input.readline()
        # strip new line
        line = line[:-1]
        line = line.split()
        R = int(line[0])
        k = int(line[1])
        N = int(line[2])

        line = input.readline()
        line = line[:-1]
        line = line.split()
        people = RingBuffer(N)
        for jj in xrange(0, N, 1):
            people.append(int(line[jj]))

        print R, k, N
        print people.get()

        # Naive approach
        money = 0
        for jj in xrange(0, R, 1) :
            num_people = 0
            counter = 0
            while ((num_people < k) and (counter < N)) :
                counter += 1
                p = people.pop()
                if (num_people + p <= k) :
                    num_people += p
                else :
                    people.push()
                    break
            money += num_people

        output.write("Case #" + str(ii + 1) + ": " + str(money) + "\n")

    input.close()
    output.close()

if __name__ == "__main__" :
    main()
