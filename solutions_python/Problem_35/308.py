import operator

def main():
    for case in range(input()):
        height, width = map(int, raw_input().split())
        
        altitude = []
        for h in range(height):
            altitude.append(list(map(int, raw_input().split())))
        
        current = [[(0, 0) for w in range(width)] for h in range(height)]
        for h in range(height):
            for w in range(width):
                direction = (0, 0)
                min_altitude = altitude[h][w]
                if 0 <= h - 1 < height and min_altitude > altitude[h - 1][w]:
                    min_altitude = altitude[h - 1][w]
                    direction = (-1, 0)
                if 0 <= w - 1 < width and min_altitude > altitude[h][w - 1]:
                    min_altitude = altitude[h][w - 1]
                    direction = (0, -1)
                if 0 <= w + 1 < width and min_altitude > altitude[h][w + 1]:
                    min_altitude = altitude[h][w + 1]
                    direction = (0, 1)
                if 0 <= h + 1 < height and min_altitude > altitude[h + 1][w]:
                    min_altitude = altitude[h + 1][w]
                    direction = (1, 0)
                current[h][w] = direction
        
        sinks = []
        for h in range(height):
            for w in range(width):
                original_node = (h, w)
                original_sink = None
                for s in sinks:
                    if original_node in s:
                        original_sink = s
                        break
                if not original_sink:
                    original_sink = set([original_node])
                    sinks.append(original_sink)
                
                next_node = tuple(map(operator.add, original_node, current[h][w]))
                if original_node == next_node or not (0 <= next_node[0] < height and 0 <= next_node[1] < width) or next_node in original_sink:
                    continue
                    
                next_sink = None
                for s in sinks:
                    if next_node in s:
                        next_sink = s
                        break
                if not next_sink:
                    original_sink.add(next_node)
                else:
                    sinks.remove(original_sink)
                    sinks.remove(next_sink)
                    sinks.append(original_sink | next_sink)
        
        lexicography = 'abcdefghijklmnopqrstuvwxyz'
        basin = [['' for w in range(width)] for h in range(height)]
        lexicography_index = -1
        for h in range(height):
            for w in range(width):
                if not basin[h][w]:
                    lexicography_index += 1
                    for s in sinks:
                        if (h, w) in s:
                            for node in s:
                                basin[node[0]][node[1]] = lexicography[lexicography_index]
        
        print "Case #%d:" % (case + 1)
        for h in range(height):
            row_string = basin[h][0]
            for w in range(1, width):
                row_string += ' ' + basin[h][w]
            print "%s" % (row_string)
            
main()
