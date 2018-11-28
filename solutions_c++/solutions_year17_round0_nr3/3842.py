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

struct IV {
	int s;
	int l;
};
bool operator<(const IV &l, const IV &r) {
	if (l.l != r.l)
		return l.l < r.l;
	return l.s < r.s;
}

int main(int argc, char* argv[])
{
	ifstream ins("in.txt");
    ofstream outs("out.txt");

    int T; ins >> T;
    F(t,0,T) {
		int N, K; ins >> N >> K;
		
		set<IV> ivs;
		IV iv = { 0, N };
		ivs.insert(iv);
		
		int ma, mi;
		F(i, 0, K) {
			IV largest = *(--ivs.end());
			ivs.erase(largest);
			IV left, right;
			left.s = largest.s;
			left.l = (largest.l-1) / 2;
			right.s = left.s + left.l + 1;
			right.l = largest.l / 2;
			if( left.l > 0 )
				ivs.insert(left);
			if( right.l > 0 )
				ivs.insert(right);
			ma = max(right.l, left.l);
			mi = min(right.l, left.l);
		}

		outs << "Case #" << t + 1 << ": " << ma << ' ' << mi << endl;
    }
    return 0;
}


