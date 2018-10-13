class forSort:
	def __init__(self, xx, yy, al):
		self.x=int(xx)
		self.y=int(yy)
		self.sum=int(xx)+int(yy)
		self.altitudes=int(al)
	def __cmp__(self, other):
		if self.altitudes != other.altitudes:
			return self.altitudes-other.altitudes
		if self.sum != other.sum:
			return self.sum-other.sum
		return other.x-self.x

T= int(raw_input())
for i in range(T):
	params= raw_input().split(' ')
	H=int(params[0])
	W=int(params[1])
	data_array=[]
	label_array=[]
	sink_array=[]
	label=0
	print 'Case #%d:'%(i+1)
	for j in range(H):
		data=raw_input().split(' ')
		for k in range(len(data)):
			data[k]=int(data[k])
		data_array.append(data)
		label_array.append(range(len(data)))
		for k in range(W):
			sink_array.append(forSort(k,j,data[k]))
	sink_array.sort()
	for sink in sink_array:
		if type(data_array[sink.y][sink.x])!=int:
			continue
		altitude=data_array[sink.y][sink.x]
		if type(label_array[sink.y][sink.x])==int:
			label_array[sink.y][sink.x]="%02d"%label
			label+=1
		if sink.y>0 and altitude<data_array[sink.y-1][sink.x] and type(label_array[sink.y-1][sink.x])==int:
			label_array[sink.y-1][sink.x]=label_array[sink.y][sink.x]
		if sink.x>0 and altitude<data_array[sink.y][sink.x-1] and type(label_array[sink.y][sink.x-1])==int:
			label_array[sink.y][sink.x-1]=label_array[sink.y][sink.x]
		if sink.y<H-1 and altitude<data_array[sink.y+1][sink.x] and type(label_array[sink.y+1][sink.x])==int:
			label_array[sink.y+1][sink.x]=label_array[sink.y][sink.x]
		if sink.x<W-1 and altitude<data_array[sink.y][sink.x+1] and type(label_array[sink.y][sink.x+1])==int:
			label_array[sink.y][sink.x+1]=label_array[sink.y][sink.x]
	labeldict=dict()
	labelalpha=ord('a')
	for label_row in label_array:
		for label in label_row:
			if labeldict.get(label)==None:
				labeldict[label]=chr(labelalpha)
				labelalpha+=1
			print labeldict[label],
		print ""