from string import lowercase

for n in xrange(int(raw_input())):
    print "Case #%d:" % (n + 1)
    grid = []
    height, width = map(int, raw_input().split())
    for i in xrange(height):
        grid.append(map(int, raw_input().split()))

    flow = [[[] for i in xrange(width)] for i in xrange(height)]

    sinks = []

    neighbours = [(0, -1), (-1, 0), (1, 0), (0, 1)]

    for y in xrange(height):
        for x in xrange(width):
            ns = [(dx + x, dy + y) for dx, dy in neighbours]
            ns = [(grid[ny][nx], i, (nx, ny))
                  for i, (nx, ny) in enumerate(ns)
                  if nx >= 0 and nx < width and ny >= 0 and ny < height]
            if ns:
                flow_value, i, (nx, ny) = min(ns)

            if ns and flow_value < grid[y][x]:
                flow[ny][nx].append((x, y))
            else:
                sinks.append((x, y))

    class Basin:
        label = None
        def __str__(self):
            return self.label

    def spread(x, y, l):
        grid[y][x] = l
        for cx, cy in flow[y][x]:
            spread(cx, cy, l)

    for x, y in sinks:
        spread(x, y, Basin())

    i = 0
    for row in grid:
        for cell in row:
            if not cell.label:
                cell.label = lowercase[i]
                i += 1
        print ' '.join(map(str, row))

