

class Case:
    Row1 = 0
    Row2 = 0
    caseNumber = 0


    def __init__(self, number, lines):
        self.caseNumber = number
        self.arrange1 = self.parse(lines[:5])
        self.arrange2 = self.parse(lines[5:])

    def parse(self, lines):

        if self.Row1 == 0:
            self.Row1 = int(lines[0])
        else:
            self.Row2 = int(lines[0])

        lines = lines[1:]

        rows = []

        for line in lines:
            values = str.split(line, ' ')
            row = []
            for val in values:
                row.append(int(val))

            rows.append(row)

        arrange = Arrangement(rows)
        return arrange

    def solve(self):
        row1 = self.arrange1.Rows[self.Row1-1]
        row2 = self.arrange2.Rows[self.Row2-1]

        matches = []

        for i in row1:
            if i in row2:
                matches.append(i)

        if len(matches) == 1:
            return "Case #{0}: {1}".format(self.caseNumber, matches[0])
        elif len(matches) > 1:
            return "Case #{0}: {1}".format(self.caseNumber, "Bad magician!")
        elif len(matches) == 0:
            return "Case #{0}: {1}".format(self.caseNumber, "Volunteer cheated!")
        else:
            return "Something done fucked up"



class Arrangement:

    def __init__(self, rows):
        self.Rows = rows