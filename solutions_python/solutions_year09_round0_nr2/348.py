import pygraph

def key_second(x):
    return x[1][1]

def get_min_indices(matrix, h, w):
    l = [((h, w), matrix[h][w]), ((h - 1, w), matrix[h - 1][w]),
        ((h, w - 1), matrix[h][w - 1]) ,((h, w + 1), matrix[h][w + 1]), ((h + 1, w), matrix[h + 1][w])]
    l = [x for x in l if None != x[1]]
    l.sort(key = key_second)
    return l[0][0]

def main():
    #bla = r"D:\Project CodeJam\Test\A-large.in"
    bla = r"D:\Project CodeJam\Test\B-large.in"
    
    f = open(bla)
    lines = f.readlines()
    f.close()

    f_write = open(r"D:\Project CodeJam\Test\output10.txt", "w")
    num_maps = int(lines[0])
    
    curr_line = 0
    for map_index in range(1, num_maps + 1):
        curr_line += 1
        line = lines[curr_line]
        
        (height, width) = tuple(int(x) for x in line.split(" "))
        matrix = []
        
        for h in range(height + 2):
            matrix.append([])
            for w in range(width + 2):    
                matrix[h].append(None)

        for h in range(1, height + 1):
            curr_line += 1
            line = lines[curr_line]
            rainage = line.split(" ")
            for w in range(1, width + 1):    
                matrix[h][w] = (False, int(rainage[w - 1]))
                
        # Now for each of the nodes I need to find the cell to which the stream goes down to

        g = pygraph.graph()
        
        # Find a better way to do this
        for h in range(1, height + 1):
            for w in range(1, width + 1):    
                g.add_nodes([(h, w)])
        
        for h in range(1, height + 1):
            for w in range(1, width + 1):    
                # calc min min_indexes rainage[w],
                (neig_h_index, neig_w_index) = get_min_indices(matrix, h, w)
                if (neig_h_index, neig_w_index) != (h, w):
                    g.add_edge((h, w),(neig_h_index, neig_w_index))
                
        letter = 'a'
        for h in range(1, height + 1):
            for w in range(1, width + 1):    
                if matrix[h][w][0]: # Already been in this node
                    continue    
                st, pre, post = pygraph.algorithms.searching.depth_first_search(g, root = (h, w))
                for (h_go, w_go) in st:
                    matrix[h_go][w_go] = (True, letter)
                letter = chr(ord(letter) + 1)
        
        new_str = "Case #%d:\n" % (map_index,)
        f_write.write(new_str)
        for h in range(1, height + 1):
            new_str = "%s\n" % " ".join([matrix[h][w_go][1] for w_go in range(1, width + 1)])
            f_write.write(new_str)
    f_write.close()
    print "Done"
    
main()