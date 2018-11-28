#include <iostream>
#include <fstream>
#include <sstream>
#include <stdlib.h>
#include <string.h>
#include <queue>
#include <unordered_map>
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
		uint64_t N,K;
		stringstream(line) >> N >> K; 

		//
		uint64_t p=0;
		priority_queue<uint64_t> q;
		unordered_map<uint64_t, uint64_t> m;
		q.push(N);
		m[N] = 1;
		uint64_t l,r,s;
		while(p<K) {
			s = q.top();
			q.pop();
			l = (s-1)/2;
			r = s/2;
			//cout << "s=" << s << " [l:r]=" << l << ":" << r << endl;
			if (l != 0) {
				if (m.count(l)==0) q.push(l);
				m[l] = (m.count(l)>0 ? m[l] : 0) + m[s]; 
			}
			if (r != 0) {
				if (m.count(r)==0) q.push(r);
				m[r] = (m.count(r)>0 ? m[r] : 0) + m[s]; 
			}
			//cout << "s=" << s << " m[l]:m[r]=" << m[l] << ":" << m[r] << endl;
			p += m[s];
			m.erase(s);
			// increment p
			//cout << "p=" << p << "[l:r]=" << l << ":" << r << endl;
		}

		opfs << r << " " << l << endl;
		cn++;
	}
}
