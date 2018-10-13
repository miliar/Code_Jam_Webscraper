
import sys
import string

# main strategy :: find sink for each cell ... or basically find labelled lower cell for each cell
		
class Map:

	basin_labels = string.ascii_lowercase;
	INFINITY = 10000;
	def __init__( self, file):
		
		self.h , self.w = file.readline().split();
		self.h , self.w = int(self.h) , int(self.w) ;	
		
		self.altitudes=[];
		self.labels=[];
		
		for row in xrange(self.h):
			self.altitudes.append(file.readline().split());
			self.labels += [[None] * self.w]

		for row in xrange(self.h):
			for col in xrange(self.w):
				self.altitudes[row][col] = int(self.altitudes[row][col]);
			
			
		self.label_index = 0;	
	
	def label_watersheds(self):
		for row in xrange(self.h):
			for col in xrange(self.w):
				if self.labels[row][col] is None:
					self.labels[row][col] = self.find_sink_label(row,col);
		

	
	def find_sink_label(self,row,col):
		#find the lower cell
		lower_cell_row, lower_cell_col = self.find_lower_cell(row,col);
		
		if lower_cell_row is not None  and lower_cell_col is not None:
			# there is a lower cell
			#print lower_cell_row,lower_cell_col
			if self.labels[lower_cell_row][lower_cell_col] is not None:
				#lower cell is already labeled
				#thus, its sink is the current sink so just use its label
			
				return self.labels[lower_cell_row][lower_cell_col] ;
			else:
				#continue with search for sink	
				
				return self.find_sink_label(lower_cell_row, lower_cell_col);
		else:
			#this cell is sink 
			
			if self.labels[row][col] is None:
				#sink not labeled yet
				#label sink
				self.labels[row][col] = self.basin_labels[self.label_index];
				
				self.label_index+=1;
			
			return self.labels[row][col];
	


	def find_lower_cell(self,row,col):
		north_row , north_col =  row -1 ,col;
		west_row , west_col = row  ,col -1;
		east_row , east_col = row  , col +1;
		south_row , south_col = row + 1 ,col;
		
		
		alt = self.get_altitude(row , col );
		
		north_alt  =  self.get_altitude(north_row , north_col )
		south_alt  = self.get_altitude(south_row , south_col)
		east_alt    = self.get_altitude(east_row , east_col )
		west_alt   =  self.get_altitude(west_row , west_col )
		
		#print north_alt,west_alt,east_alt,south_alt
		
		min_alt = min([north_alt,west_alt,east_alt,south_alt]) ;
		#print min_alt
		if min_alt >= alt:
			# sink found
			
			return None,None;
			
			
		if north_alt == min_alt:
			#print "north_row , north_col" , north_row , north_col;
			return north_row , north_col;

		if west_alt == min_alt:
			#print "west_row , west_col " , west_row , west_col;
			return west_row , west_col;

		if east_alt == min_alt:
			#print "east_row , east_col " ,east_row , east_col;
			return  east_row , east_col ;
		
		if south_alt == min_alt:
			#print "south_row , south_col" , south_row , south_col;
			return  south_row , south_col ;

		


	def get_altitude(self,row,col):
		if row >= self.h or row < 0:
			return self.INFINITY;
		if col >= self.w or col < 0:
			return self.INFINITY;	
		return self.altitudes[row][col];
		
	
	def string(self):
		row_string = ""
		for row in xrange(self.h):
			for col in xrange(self.w):
				row_string+= ("%s ") %self.labels[row][col];
			if row != self.h -1:	
				row_string+="\n"
		return row_string;
			

def solve_watershed_labeling_problem(input_file_path , output_file_path):
		
	input_file = open(input_file_path,"r");
	output_file = open(output_file_path,"w");
	
	map_count = int(input_file.readline());
	
	for index in xrange(map_count):
		map = Map(input_file);
		map.label_watersheds();
		labled_map_str = map.string();
		solution_string = "Case #%d:\n%s"%(index +1 , labled_map_str)
		print solution_string;
		output_file.write(solution_string+"\n");
	
	
	input_file.close()
	output_file.close()

	
def  start_me_up():
	if len(sys.argv) == 1:
		print "Usage:"
		print "%s input_file_path [output_file_path]" % ( sys.argv[0]);		
		print "Note: Solution is output to console too." ;		
		
	elif len(sys.argv) == 2:
		solve_watershed_labeling_problem(sys.argv[1], sys.argv[1]+'.out');
	
	elif len(sys.argv) >= 3:	
		solve_watershed_labeling_problem(sys.argv[1], sys.argv[2]);
		


if __name__ == "__main__":
	start_me_up();














