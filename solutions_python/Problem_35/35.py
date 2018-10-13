import string

inputFile = "B-large.in";
outputFile = "B-large.out";


def main():	
	fdin = open(inputFile);
	fdout = open(outputFile, 'wb');
	
	casecountString = fdin.readline();
	caseCount = int(casecountString);
		
	for k in range(caseCount):
		HWline = fdin.readline();
		H = int(HWline.split()[0]);
		W = int(HWline.split()[1]);
		matrix=[];
		for i in range(H):
			line = fdin.readline();
			cline = line.split();
			for j in range(W):
				cline[j] = int(cline[j]);
			matrix.append(cline);
			
		result = processCase(matrix, H, W);
		resultLine = "Case #" + str(k+1) + ": " + "\n";
		fdout.write(resultLine);
		for m in range(H):
			resultLine = ''
			for n in range(W):
				resultLine = resultLine + result[m][n] + ' ';
			resultLine = resultLine + '\n';
			fdout.write(resultLine);

def processCase(mat, H, W):
	sets = {};
	roots = [];
	results = mat;
	for i in range(H*W):
		roots.append(-1);
		sets[i]=[i];
	for m in range(H):
		for n in range(W):
			minheight=mat[m][n];
			xdirection=0;
			ydirection=0;
			if m>0 and mat[m-1][n]<minheight:
				minheight=mat[m-1][n];
				xdirection=-1;
				ydirection=0;
			if n>0 and mat[m][n-1]<minheight:
				minheight=mat[m][n-1];
				xdirection=0;
				ydirection=-1;
			if n<W-1 and mat[m][n+1]<minheight:
				minheight=mat[m][n+1];
				xdirection=0;
				ydirection=1;
			if m<H-1 and mat[m+1][n]<minheight:
				minheight=mat[m+1][n];
				xdirection=1;
				ydirection=0;
			pos=m*W+n;
			if xdirection+ydirection == 0:
				#sink
				roots[pos]=pos;
			else:
				flowpos=(m+xdirection)*W+n+ydirection;
				if roots[flowpos] == -1:
					rootpos=flowpos;
				else:
					rootpos=roots[flowpos];
				for item in sets[pos]:
					roots[item]=rootpos;
				sets[rootpos]= sets[rootpos] + sets[pos];
				sets[pos]=[];
	letters={};
	index=0;
	for z in range(H*W):
		if not letters.has_key(roots[z]): 
			letters[roots[z]]=string.ascii_lowercase[index];
			index=index+1;
		results[z/W][z%W]=letters[roots[z]];
	return results;
				
				
				
	

if __name__ == "__main__":
    main()
