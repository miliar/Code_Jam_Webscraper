class ProblemB:

    def Solve(self, file_in, file_out, max_labels):
        self.max_labels = max_labels
        self.__Read(file_in)
        for i_map, map in enumerate(self.maps):
            self.__SolveCase(map, self.maps_h[i_map], self.maps_w[i_map], self.labels[i_map])
        self.__Write(file_out)
        
    def __Read(self, file_in):
        f = open(file_in, "r")
        self.number_of_maps = int(self.__ReadLineAndWithoutBreaks(f))
        self.maps = []
        self.maps_h = []
        self.maps_w = []
        self.labels = []
        for i_map in range(0, self.number_of_maps):
            map_dimensions = self.__ReadLineAndWithoutBreaks(f)
            map_dimensions_data = map_dimensions.split(" ")
            map_h = int(map_dimensions_data[0])
            map_w = int(map_dimensions_data[1])
            self.maps_h.append(map_h)
            self.maps_w.append(map_w)
            map = []
            map_labels = []
            for i_row in range(0, map_h):
                row = []
                row_labels = []
                row_cols = self.__ReadLineAndWithoutBreaks(f)
                row_cols_data = row_cols.split(" ")
                for i_col in range(0, map_w):
                    row.append(row_cols_data[i_col])
                    row_labels.append(-1)
                map.append(row)
                map_labels.append(row_labels)
            self.maps.append(map)
            self.labels.append(map_labels)
        f.close()
        
    def __ReadLineAndWithoutBreaks(self, f):
        return f.readline().rstrip("\n\r")
        
    def __SolveCase(self, map, h, w, labels):
        sinks = self.__GetSinks(map, h, w)
        flows = self.__GetFlows(map, h, w)
        cells = []
        number_of_cells = 0
        for i_sink, sink in enumerate(sinks):
            labels[sink[0]][sink[1]] = i_sink
            cells.append(sink)
            number_of_cells+= 1
        while number_of_cells > 0:
            cell = cells.pop(0)
            number_of_cells-= 1
            label = labels[cell[0]][cell[1]]
            neighboring_cells = self.__GetNeighboringCellsInOrder(cell[0], cell[1], map, h, w)
            for neighboring_cell in neighboring_cells:
                if labels[neighboring_cell[0]][neighboring_cell[1]] == -1 and self.__FlowsTo(neighboring_cell, cell, flows):
                    labels[neighboring_cell[0]][neighboring_cell[1]] = label
                    cells.append(neighboring_cell)
                    number_of_cells+= 1
        self.__TranslateIds(map, labels, h, w)
        
    def __GetSinks(self, map, h, w):
        sinks = []
        for row, altitudes in enumerate(map):
            for col, altitude in enumerate(altitudes):
                is_sink = row == 0 or altitude <= map[row - 1][col]
                is_sink = is_sink and (col == 0 or altitude <= map[row][col - 1])
                is_sink = is_sink and (row == h - 1 or altitude <= map[row + 1][col])
                is_sink = is_sink and (col == w - 1 or altitude <= map[row][col + 1])
                if is_sink:
                    sinks.append((row, col))
        number_of_sinks = len(sinks)
        assert number_of_sinks > 0 and number_of_sinks <= self.max_labels
        return sinks
        
    def __GetFlows(self, map, h, w):
        flows = []
        for row, altitudes in enumerate(map):
            row_flows = []
            for col, altitude in enumerate(altitudes):
                row_flows.append(self.__GetFlow(row, col, map, h, w))
            flows.append(row_flows)
        return flows
        
    def __GetFlow(self, row, col, map, h, w):
        cells = self.__GetNeighboringCellsInOrder(row, col, map, h, w)
        min_cell = None
        for cell in cells:
            if min_cell == None or map[cell[0]][cell[1]] < map[min_cell[0]][min_cell[1]]:
                min_cell = cell
        return min_cell
        
    def __GetNeighboringCellsInOrder(self, row, col, map, h, w):
        cells = []
        if row > 0:
            cells.append((row - 1, col))
        if col > 0:
            cells.append((row, col - 1))
        if col < w - 1:
            cells.append((row, col + 1))
        if row < h - 1:
            cells.append((row + 1, col))
        return cells
        
    def __FlowsTo(self, from_cell, to_cell, flows):
        from_cell_flows_to = flows[from_cell[0]][from_cell[1]]
        return from_cell_flows_to != None and from_cell_flows_to[0] == to_cell[0] and from_cell_flows_to[1] == to_cell[1]
        
    def __TranslateIds(self, map, labels, h, w):
        ids = {}
        c_code = 97
        for row, altitudes in enumerate(map):
            for col, altitude in enumerate(altitudes):
                id = labels[row][col]
                assert id != -1
                if not id in ids:
                    ids[id] = chr(c_code)
                    c_code+= 1
                labels[row][col] = ids[id]
        
    def __Write(self, file_out):
        f = open(file_out, "w")
        for i_case in range(0, self.number_of_maps):
            if(i_case > 0):
                f.write("\n")
            line = "Case #%i:" % (i_case + 1)
            f.write(line + "\n")
            print line
            case_labels = self.labels[i_case]
            for i_row, row_labels in enumerate(case_labels):
                line = ""
                for i_label, label in enumerate(row_labels):
                    if i_label > 0:
                        line+= " "
                    line+= label
                if(i_row > 0):
                    f.write("\n")
                f.write(line)
                print line
        f.close()

problem_b = ProblemB()
#problem_b.Solve("B-example.in", "B-example.out", 26)
#problem_b.Solve("B-small-attempt0.in", "B-small-attempt0.out", 2)
#problem_b.Solve("B-small-attempt1.in", "B-small-attempt1.out", 2)
#problem_b.Solve("B-small-attempt2.in", "B-small-attempt2.out", 2)
#problem_b.Solve("B-small-attempt3.in", "B-small-attempt3.out", 2)
#problem_b.Solve("B-small-attempt4.in", "B-small-attempt4.out", 2)
problem_b.Solve("B-small-attempt5.in", "B-small-attempt5.out", 2)
#problem_b.Solve("B-large.in", "B-large.out", 26)
