#include "stdafx.h"

#include <math.h> 
#include <algorithm> 
#include <string> 
#include <vector> 
#include <map> 
#include <set> 
#include <sstream> 
#include <iostream> 
#include <ctype.h> 
#include <list>
#include <queue>
#include <numeric>
#include <fstream>
#include <iomanip>  

using namespace std; 

#define VS vector<string> 
#define VI vector<int> 
#define VD vector<double>

#define F(v,s,e) for( int v = (int)(s); v < (int)(e); ++v ) 
#define SET00(x) memset( (x), 0, sizeof(x));
#define SETFF(x) memset( (x), 0xff, sizeof(x));

#define ISS istringstream 
#define OSS ostringstream 

#define i64 long long
#define VI64 vector<i64>

const double PI = 4*atan(1.); 
const double EPS = 1.E-12;

int ones( i64 x ) { return x ? 1 + ones( x&(x-1) ) : 0; }

bool assert( bool b ) { 
    if( !b ) {
        cout << "Assertion failed!" << endl;
        exit(1);
    }
}

struct CYL {
	double r, h;
};
bool PP(const CYL &l, const CYL &r) {
	return l.r * l.h > r.r * r.h;
}
bool operator<(const CYL &l, const CYL &r) {
	if (l.r == r.r)
		return l.h > r.h;
	return l.r > r.r;
}

CYL cyls[1000], ocyls[1000];

int main(int argc, char* argv[])
{
	ifstream ins("in.txt");
    ofstream outs("out.txt");

    int T; ins >> T;
    F(t,0,T) {
		int N, K; ins >> N >> K;
		F(i, 0, N)
			ins >> ocyls[i].r >> ocyls[i].h;
		sort(ocyls, ocyls + N);

		double best = 0.;
		F(s, 0, N) F(e, s + K, N + 1) {
			memcpy(cyls, ocyls, sizeof(cyls));
			double surf = PI*cyls[s].r*cyls[s].r;
			sort(cyls + s + 1, cyls + e, &PP);
			F(i, s, s + K)
				surf += 2 * PI*cyls[i].r*cyls[i].h;
			best = max(best, surf);
		}

		outs << std::setprecision(32) << "Case #" << t + 1 << ": " << best << endl;
    }
    return 0;
}


