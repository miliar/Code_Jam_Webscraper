#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <string.h>
using namespace std;

void pr_d(int d[], int size, ofstream* os) {
	int nonzero=0;
	for (int i=0; i<size; i++) {
		if (nonzero || (d[i] != 0)) {
			nonzero = 1;
			(*os) << d[i];
		}
	}
	(*os) << endl;
}

int main(int argc, char *argv[]) {
	string ipfn,opfn;
	ifstream ipfs;
	ofstream opfs;

	//cout << "Have " << argc << " arguments:" << endl;
	for (int i=0; i<argc; i++) {
		//cout << "argv[" << i << "]: "<<  argv[i] << endl;
	}
	ipfn = argv[1]; 
	ipfs.open(ipfn.c_str());

	opfn = argv[2]; 
	opfs.open(opfn.c_str());

	string line;
	getline(ipfs, line);

	int T;
	T = atoi(line.c_str());

	int cn=1;
	char ic;
	while (cn <=T && ipfs.peek() != EOF) {
		opfs << "Case #" << cn << ": ";
		getline(ipfs, line);
		int N;
		int sz = line.length();
		int d[sz+1];
		d[0] = 0;
		N = atoi(line.c_str());
		for (int i=0; i<sz; i++) {
			char c;
			c = line[i];
			d[i+1] = atoi(&c);
		}
		int i=1;
		while (i<sz+1) {
			if (d[i-1]<=d[i]) {
				i++;
			} else {
				d[i-1]--;
				for (int k=i; k<sz+1; k++) d[k]=9;
				i--;
			}
		}
		pr_d(d, sz+1, &opfs);
		cn++;
	}

}
