# from application.app.folder.file import func_name
import csv

def ReadFile(filename, delimit,data_type = 'float', verbose = False):
	MyList = list(csv.reader(open(filename,"rb"),delimiter=delimit))
	for i, vali in enumerate(MyList):
		for j, valj in enumerate(vali):
			if data_type == 'int': 
				MyList[i][j] = int(MyList[i][j])
			if data_type == 'float':
				MyList[i][j] = float(MyList[i][j])
			if verbose:
				print MyList[i][j],
		if verbose:
			print 
	return MyList

def WriteCaseFile(filename, caselist, verbose = False):
	f = open(filename, 'w')
	for i, val in enumerate(caselist):
		f.write("Case #" + str(i+1) +": " + str(val) + "\n")
		if verbose:
			print "Case #" + str(i+1) +": " + str(val) 
def WriteCaseFileMines(filename, caselist, verbose = False):
	f = open(filename, 'w')
	for i, val in enumerate(caselist):
		if val == "\nImpossible":
			f.write("Case #" + str(i+1) +": " + str(val) + "\n")
			# if verbose:
			# 	print "Case #" + str(i+1) +": " + str(val) 
		else:
			f.write("Case #" + str(i+1) + ":\n")
			for j, jval in enumerate(val):
				for k, kval in enumerate(val[j]):
					f.write(kval)
				f.write("\n")
				# f.write	
			# print