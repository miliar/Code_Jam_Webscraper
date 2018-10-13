#!/usr/bin/python


def parse(D,i):
    Node = {};
    if(D[i] == "("):
	Node['weight'] = float(D[i+1]);

	if(D[i+2] != ")"):
	    Node['feature'] = D[i+2];
	    Node['left'] = parse(D,i+3)
	    c = 1;
	    for j in range(i+4,len(D)):
		if(D[j] == "("):
		    c += 1;
		if(D[j] == ")"):
		    c -= 1;
		if c == 0:
		    break;
	    Node['right'] = parse(D,j+1)
	else:
	    Node['feature'] = None;
    else:
	return None;
    return Node;

def calcP(T, feat):
    P = 1.0;
    while T != None:
	P *= T['weight'];
	if T['feature'] == None:
	    return P;
	if(T['feature'] in feat):
	    T = T['left'];
	else:
	    T = T['right'];


def doCase():
    L = input();
    D = "";

    for i in range(L):
	D += raw_input();
    D = D.replace("(", " ( ").replace(")"," ) ");

    T = parse(D.split(),0);

    A = input();
    for i in range(A):
	X = raw_input().split();
	name = X[0];
	feat = X[2:];
	print "%0.7f" % calcP(T, feat);




N = input();

for i in range(N):
    print "Case #%d: " % (i+1)
    doCase();