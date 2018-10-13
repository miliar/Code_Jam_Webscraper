from array import array
import fileinput

def run():
    output = None
    case = 0
    for line in fileinput.input():
        if fileinput.isfirstline():
            filename = fileinput.filename().replace(".in", "")
            output = open(filename + ".out", 'w')
            continue
        case += 1

        line = line.replace("\n", "")

        scenario = Scenario(line)
        result = scenario.calculate()

        output.write("Case #%s: %s\n" % (case, result))

    output.close()





class Scenario():
    def __init__(self, line):
        parts = line.split(" ")
        assert len(parts) == 2
        self.max_shyness = long(parts[0])
        self.shyness = []
        for char in parts[1]:
            self.shyness.append(long(char))

    def calculate(self):
        need_to_invite = 0
        standing = 0
        for shyness_level in xrange(self.max_shyness + 1):
            if standing < shyness_level:
                # need to invite some more people
                more = shyness_level - standing
                need_to_invite += more
                standing += more

            assert standing >= shyness_level

            standing += self.num_people(shyness_level)

        return need_to_invite

    def num_people(self, shyness_level):
        return self.shyness[shyness_level]



if __name__ == '__main__':
    run()
