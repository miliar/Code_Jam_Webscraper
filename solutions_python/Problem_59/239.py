#!/usr/bin/python

tree = {};

def createDir(dirName, tree):
	folders = dirName.split('/');
	#print(folders);
	if ((len(folders) <= 0) or (folders[0] == '')):
		#print("EMPTY");
		return [0, tree];
	else:
		if folders[0] in tree:
			#print("FOUND");
			result = createDir( '/'.join(map(str,folders[1:])), tree[folders[0]] );
			tree[folders[0]] = result[1];
			return [result[0], tree];
		else:
			#print("NEW");
			result = createDir( '/'.join(map(str,folders[1:])), {} );
			tree[folders[0]] = result[1];
			return [result[0]+1, tree];

T = int( raw_input() );
for caseN in range(1,T+1):
	(N,M) = map(int,raw_input().split())
	tree = {};
	for i in range(N):
		result = createDir(raw_input()[1:],tree);
		#print("Found {0} dir(s).".format(result[0]));
		tree = result[1];
	numReq = 0;
	for i in range(M):
		result = createDir(raw_input()[1:],tree);
		#print("Created {0} dir(s).".format(result[0]));
		numReq += result[0];
		tree = result[1];
	print("Case #{0}: {1}".format(caseN,numReq));

