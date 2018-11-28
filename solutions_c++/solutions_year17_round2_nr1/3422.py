#include <iostream>
#include <fstream>
#include <sstream>
#include <stdlib.h>
#include <string.h>
#include <queue>
#include <unordered_map>
using namespace std;

ifstream ipfs;
ofstream opfs;

int main(int argc, char *argv[]) {
	string ipfn,opfn;


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
		int D,N;
		double result;
		stringstream(line) >> D >> N;
		for (int i=0; i<N; i++) {
			getline(ipfs, line);
			stringstream ss(line);
			uint64_t k,s;
			double a;
			ss >> k >> s; 
			a = (double)D*s/(D-k);
			//cout << "Horse i=" << i << " k=" << k << " s=" << s << " a=" << a << endl;
			if (i==0) result = a;
			else if (a<result) result=a;
		}
		opfs.precision(6);
		opfs << fixed << result << endl;
		cn++;
	}
}
