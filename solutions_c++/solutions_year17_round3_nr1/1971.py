#include <iostream>
#include <fstream>
#include <sstream>
#include <stdlib.h>
#include <string.h>
#include <queue>
#include <unordered_map>
#include <math.h>
using namespace std;


ifstream ipfs;
ofstream opfs;

class pancake {
	public:
	uint64_t radius;
	uint64_t height;
	uint64_t base;
	uint64_t side;
	void init() {
		side = radius*height*2;
		base = radius*radius+side;
	}
};

pancake base;

struct Comparebase {
    bool operator()(pancake const & p1, pancake const & p2) {
        // return "true" if "p1" is ordered before "p2", for example:
        return p1.base < p2.base;
    }
};
struct Compareradius {
    bool operator()(pancake const & p1, pancake const & p2) {
        // return "true" if "p1" is ordered before "p2", for example:
        return p1.radius < p2.radius;
    }
};
struct Compareside {
    bool operator()(pancake const & p1, pancake const & p2) {
        // return "true" if "p1" is ordered before "p2", for example:
        return p1.side < p2.side;
    }
};
uint64_t others(pancake const& p) {
	if (p.radius < base.radius) return p.side;
	else return (p.base - base.radius*base.radius);
}
struct Compareothers {
    bool operator()(pancake const & p1, pancake const & p2) {

        return others(p1) < others(p2);
    }
};
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
		uint64_t areamax;
		areamax=0;
		cout << "Case #" << cn << ": ";
		getline(ipfs, line);
		int N, K;
		stringstream ss(line);
		ss >> N >> K;
		priority_queue< pancake, vector<pancake>, Compareradius > pq;
		for (int i=0; i<N; i++) {
			getline(ipfs, line);
			pancake* p = new pancake;
			stringstream ss(line);
			ss >> p->radius >> p->height;
			p->init();
			pq.push(*p);
		}
		while (pq.size() >= K) {
			uint64_t area;
			base = pq.top();
			pq.pop();
			area = base.base;
			//cout << "First P= " << base.radius << " " << base.height << " pq.size =" << pq.size() << endl;
			priority_queue< pancake, vector<pancake>, Compareradius > pqtemp;
			pqtemp = pq;
			priority_queue< pancake, vector<pancake>, Compareside > pqs;
			for (int i=0; pqtemp.size()!=0; i++) {
				pqs.push(pqtemp.top());
				pqtemp.pop();
			}
			for (int i=0; i<K-1; i++) {

				pancake p = pqs.top();
				//cout << "Next  P= " << p.radius << " " << p.height << endl;
				area = area + p.side;
				pqs.pop();
			}
			//cout << "final area=" << area << endl;
			if (area > areamax) {
				//cout << "THIS IS MAX" << endl;
				areamax = area;
			}
		}
		cout.precision(9);
		double r = areamax*M_PI;
		cout << fixed << r << endl;
		cn++;
	}
}
