	
def visit( map, H, W, n, output, currentbasin ):
	y = n[0]; x = n[1];	
	
	if output[y][x] == '':
				
		min = [999999, 999999, 999999];
		if y > 0 and min[0] > map[y-1][x]:
			min = [map[y-1][x], y-1, x];		
		if x > 0 and min[0] > map[y][x-1]:
			min = [map[y][x-1], y, x-1];			
		if x < W-1 and min[0] > map[y][x+1]:
			min = [map[y][x+1], y, x+1];		
		if y < H-1 and min[0] > map[y+1][x]:
			min = [map[y+1][x], y+1, x];
			
		if min[0] < map[y][x]:
			output[y][x] = visit( map, H, W, [min[1], min[2]], output, currentbasin );
		else:			
			output[y][x] = currentbasin[0];
			currentbasin[0] = chr(ord(currentbasin[0]) + 1);
				
	return output[y][x];

	
def tobasins( map, H, W ):
	
	currentbasin = ['a'];
	output = [];
	
	for y in xrange( H ):
		output.append([]);
		for x in xrange( W ):
			output[y].append('');
	
	for y in xrange( H ):
		for x in xrange( W ):
		
			visit( map, H, W, [y, x], output, currentbasin );	
			
	return output;

f = open("B-large.in");

T = int( f.readline()[:-1] );

for t in xrange( T ):
		
	H, W = f.readline()[:-1].split(" ");
	H = int(H); W = int(W);

	map = [];
	for i in xrange( H ):
		map.append( f.readline()[:-1].split(" ") );

	for y in xrange( H ):
		for x in xrange( W ):
			map[y][x] = int(map[y][x]);			
			
	print "Case #" + str(t+1) + ":";
	basins = tobasins( map, H, W );
	for x in basins:
		print " ".join(x);

