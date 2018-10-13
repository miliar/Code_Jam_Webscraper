import re
import sys

if __name__ == '__main__':
	#in_filename = "B-small.in"
	#in_filename = "B-dummy.in"
	in_filename = "B-large.in"
	#out_filename = "B-small.out"
	out_filename = "B-large.out"
	
	in_file = open(in_filename, 'r')
	out_file = open(out_filename, 'w')

	num_cases = int(in_file.readline())
	for c in range(0,num_cases):
		H,W = [int(x) for x in in_file.readline().split(' ')]
		map = []
		for h in range(0,H):
			map = map + [int(x) for x in in_file.readline().split(' ')]
		label = range(0,H*W)
		assoc = [-1]*H*W 
		
		for h in range(0,H):
			for w in range(0,W):
				cursor = h*W + w
				min = sys.maxint
				way = -1
				
				# Flow backward - add to association map
				pos1 = (h-1)*W + w
				if h != 0 and map[pos1] < min:
					min = map[pos1]
					way = 1

				pos2 = h*W + w - 1
				if w != 0 and map[pos2] < min:
					min = map[pos2]
					way = 2

				# Flow forward in loop direction - just assigned it
				pos3 = h*W + w + 1
				if (w + 1) < W and map[pos3] < min:
					min = map[pos3]
					way = 3

				pos4 = (h + 1)*W + w
				if (h + 1) < H and map[pos4] < min:
					min = map[pos4]
					way = 4
				
				# If is Sink
				if min < map[cursor]:
					if way == 1:
						assoc[label[cursor]] = label[pos1]
					elif way == 2:
						assoc[label[cursor]] = label[pos2]
					elif way == 3:
						#label[pos3] = label[cursor]
						assoc[label[cursor]] = label[pos3]
					elif way == 4:
						#label[pos4] = label[cursor]
						assoc[label[cursor]] = label[pos4]

		# Do paths compression
		#print "Before", assoc
		for ind in range(0,len(assoc)):
			next = assoc[ind]
			last = next
			while next != -1:
				last = next
				next = assoc[next]
			assoc[ind] = last 
		#print "Compress", assoc

		# Final relabel
		out_file.write("Case #%d:\n" % (c+1))
		char_map = {}
		running = ord('a') 
		for h in range(0,H):
			for w in range(0,W):
				cursor = h*W + w
				if assoc[label[cursor]] != -1:
					label[cursor] = assoc[label[cursor]]
				if label[cursor] not in char_map:
					char_map[label[cursor]] = running
					running = running + 1
				
			#print label[h*W:h*W + W]
			out_file.write(' '.join([chr(char_map[x]) for x in label[h*W:h*W + W]]))
			out_file.write('\n')


	out_file.close()

