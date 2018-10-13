import logging

class Map:
    
    def __init__(self,  height,  width,  topo):
        self.height = height
        self.width = width
        self.topo = topo
        self.basins = a = [ [ 0 for x in range(width)] for y in range(height) ]
        self.next_basin= 'a'
        logging.debug((self.topo))
        logging.debug((self.basins))
    
    def process(self):
        for y in range(self.height):
            for x in range(self.width):
                self.process_cell(x, y,  0)
                
        return '\n'.join(' '.join(row) for row in self.basins)
        
    def process_cell(self, x, y,  indent):
        
        s = indent * 2 *' ' + '- '
        
        logging.debug((s +'process: ',  x , y,  self.topo[y][x]))
        
        if self.basins[y][x] != 0:
            logging.debug((s +'got:', x, y, self.basins[y][ x]))
            return self.basins[y][x]

        lowest_altitude = self.topo[y][x];
        flowto_where = 'sink';
        
        if y > 0 and lowest_altitude > self.topo[y - 1][ x]:
            logging.debug((s +'north'))
            lowest_altitude = self.topo[y - 1][ x];
            flowto_where = y - 1,  x
        if x > 0 and lowest_altitude > self.topo[y][ x - 1]:
            logging.debug((s +'west'))
            lowest_altitude = self.topo[y][ x - 1]
            flowto_where = y,  x -1
        if x < self.width - 1 and lowest_altitude > self.topo[y][ x + 1]:
            logging.debug((s +'east'))
            lowest_altitude = self.topo[y][ x + 1]
            flowto_where = y,  x + 1
        if y < self.height - 1 and lowest_altitude > self.topo[y + 1][ x]:
            logging.debug((s +'south'))
            lowest_altitude = self.topo[y + 1][ x];
            flowto_where = y + 1,  x

        if flowto_where == 'sink':
            logging.debug((s +'sink'))
            self.basins[y][ x] = self.next_basin
            self.next_basin = chr(ord(self.next_basin) + 1)
        else:
            self.basins[y][ x] = self.process_cell(flowto_where[1],  flowto_where[0],  indent + 1)
            
        logging.debug((s +'return:', x, y, self.basins[y][ x]))
        return self.basins[y][ x]
        

count = int(raw_input())
for i in range(count):
    (H,  W) = map(int, raw_input().split())
    topo = []
    for y in range(H):
        topo.append(map(int, raw_input().split())) 
    basins = Map(H,  W,  topo)
    print  'Case #' + str(i+1)  + ':\n' + basins.process()


