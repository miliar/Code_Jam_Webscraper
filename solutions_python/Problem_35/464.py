
class Watersheds:
    def __init__(self, map, width, height):
        self.width = width
        self.height = height
        
        self.letter = 97
        
        self.map = []
        self.map_create(map)
        self.map[0][0].letter = self.get_letter()
        
        self.process()

    def map_create(self, map):
        self.map = []
        
        for y in range(self.height):
            self.map.insert(y, [])
            
            for x in range(self.width):
                self.map[y].insert(x, WatershedsCell(x, y, map[y][x]))

    def get_letter(self):
        char_letter = chr(self.letter)
        self.letter += 1
        return char_letter

    def process(self):
        for y in range(self.height):
            for x in range(self.width):
                cell = self.map[y][x]
                flow = self.flows(x, y)
                
                if not cell.letter and cell.fin:
                    for fin in cell.fin:
                        if fin.letter:
                            cell.letter = fin.letter
                            break
                
                if flow:
                    flow.fin.append(cell)
                    
                    if not flow.letter:
                        flow.letter = cell.letter
                    if not cell.letter:
                        cell.letter = flow.letter
                else:
                    cell.sink = True
                    
                    if not cell.letter:
                        cell.letter = self.get_letter()
                        self.set_letter_rec(cell, cell.letter)
        
        for y in range(self.height):
            for x in range(self.width):
                cell = self.map[y][x]
                self.set_letter_rec(cell, cell.letter)

    def set_letter_rec(self, cell, letter):
        if cell.fin:
            for fin in cell.fin:
                if not fin.letter:
                    fin.letter = letter
                    self.set_letter_rec(fin, letter)

    def flows(self, x, y):
        cell = cmin = self.map[y][x]
        
        for neighbor in self.get_neighbors(x, y):
            if neighbor:
                if neighbor.alt < cmin.alt:
                    cmin = neighbor
        
        if cell is cmin:
            return None
        return cmin

    def get_neighbors(self, x, y):
        return [
            self.get_neighbor_north(x, y),
            self.get_neighbor_west(x, y),
            self.get_neighbor_east(x, y),
            self.get_neighbor_south(x, y)
        ]

    def get_neighbor_north(self, x, y):
        if y - 1 >= 0 and y - 1 < self.height:
            return self.map[y - 1][x]
        return None

    def get_neighbor_west(self, x, y):
        if x - 1 >= 0 and x - 1 < self.width:
            return self.map[y][x - 1]
        return None

    def get_neighbor_east(self, x, y):
        if x + 1 >= 0 and x + 1 < self.width:
            return self.map[y][x + 1]
        return None

    def get_neighbor_south(self, x, y):
        if y + 1 >= 0 and y + 1 < self.height:
            return self.map[y + 1][x]
        return None

    def answer(self):
        r = ''
        for y in range(self.height):
            row = ''
            for x in range(self.width):
                cell = self.map[y][x]
                row += cell.letter + ' '
            r += row.strip() + '\n'
        return r

class WatershedsCell:
    def __init__(self, x, y, alt):
        self.x = x
        self.y = y
        self.alt = int(alt)
        self.letter = None
        self.sink = False
        self.fin = []

def main():
    FILENAME = 'B-small-attempt0'
    
    output = open(FILENAME + '.out', 'w')
    lines = open(FILENAME + '.in', 'r').readlines()
    
    maps = int(lines[0])
    mapin = False
    mapn = 0
    
    lines = lines[1:]
    
    for i in range(len(lines)):
        line = lines[i].strip()
        
        if not mapin:
            parts = line.split()
            
            mapwidth = int(parts[1])
            mapheight = int(parts[0])
            mapin = True
            mapi = 0
            map_ = []
            mapn += 1
        else:
            mapi += 1
            map_.append(line.split())
            
            if mapi == mapheight:
                mapin = False
                
                w = Watersheds(map_, mapwidth, mapheight)
                
                output.write("Case #%d:\n" % (mapn))
                output.write(w.answer())
    
    output.close()

if __name__ == '__main__':
    main()