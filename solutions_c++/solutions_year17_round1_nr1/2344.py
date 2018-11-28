#include <iostream>
#include <fstream>
#include <sstream>
#include <stdlib.h>
#include <string.h>
using namespace std;

void pr_d(char** d, int R, int C) {
	for (int i=0; i<R; i++) {
		for (int j=0; j<C; j++) {
			cout << d[i][j];
		}
		cout << endl;
	}
}

int main(int argc, char *argv[]) {
	string ipfn,opfn;
	ifstream ipfs;
	ofstream opfs;

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
		opfs << "Case #" << cn << ": "<<endl;
		getline(ipfs, line);
		int R,C;
		stringstream(line) >> R >> C; 
		char arr[R][C];
		for (int i=0; i<R; i++) {
			getline(ipfs, line);
			for (int j=0; j<C; j++) {
				arr[i][j] = line[j]; 
			}
		}



		char c;
		c = '?';
		int s_i=0;
		int s_j=0;
		for (int i=0; i<R; i++) {
			for (int j=0; j<C; j++) {
				if (c == '?' && arr[i][j] == '?') {
				} else
				if (c == '?' && arr[i][j] != '?') {
					// found first match
					c = arr[i][j];
					for (int k=0; k<=j; k++) {
						arr[i][k] = c;
					}
				} else 
				if (c != '?' && arr[i][j] == '?') {
					arr[i][j] = c;
				} else 
				if (c != '?' && arr[i][j] != '?') {
					c = arr[i][j];
				}
			}
			// end of row
			c = '?';
		}

		int fnz=-1;
		for (int i=0; i<R; i++) {
			if (fnz == -1 && arr[i][0] != '?') {
				fnz = i;
				if (fnz != 0) {
					for (int k=0; k<fnz; k++) {
						for (int l=0; l<C; l++) {
							arr[k][l] = arr[fnz][l];
						}
					}
				}
			} else 
			if (arr[i][0] == '?' && fnz != -1) {
				for (int j=0; j<C; j++) {
					arr[i][j] = arr[i-1][j];
				}
			}
		}
		






		for (int i=0; i<R; i++) {
			for (int j=0; j<C; j++) {
				opfs << arr[i][j];
			}
			opfs << endl;
		}
		cn++;
	}
}
