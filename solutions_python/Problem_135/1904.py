with open("input") as f:
	content = f.readlines()

case_count = 0
entry_count = None
target_row = None
row_count = 0
first_row = None
second_row = None

def check_rows():
	global case_count,first_row,second_row
	case_count+=1
	nk=list(set(first_row).intersection(second_row))
	if len(nk)==1:
		print "Case #%s: %s"%(case_count,nk[0])
	elif len(nk)>0:
		print "Case #%s: Bad magician!"%case_count
	elif len(nk)==0:
		print "Case #%s: Volunteer cheated!"%case_count

for index,line in enumerate(content):
	line = line.strip()
	if index==0:
		entry_count = int(line)
	else:
		if target_row is None:
			target_row = int(line)
		elif line.find(" ")!=-1:
			row_count+=1
			if row_count == target_row:
				if first_row is None:
					first_row = line.split(" ")
				else:
					second_row = line.split(" ")
		else:
			if second_row is not None:
				check_rows()
				first_row=second_row=target_row=None
			row_count=0
			target_row = int(line)


check_rows()