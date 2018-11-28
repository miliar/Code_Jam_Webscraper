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

char a[25][25];
char lasti;

int counti(int ys, int xs, int ye, int xe) {
	int ret = 0;
	F(y,ys,ye) F(x,xs,xe)
		if (a[y][x] != '?') {
			lasti = a[y][x];
			++ret;
		}
	return ret;
}

void solve(int ys, int xs, int ye, int xe) {
	if (xs == xe || ys == ye)
		return;
	int dx = 1, dy = 1, n = a[ys][xs] != '?' ? 1 : 0;
	while( xs+dx <= xe && ys+dy <= ye && counti(ys, xs, ys + dy, xs + dx) < 2 )
		++dx, ++dy;
	--dx; --dy;
	if(ys + dy < ye && counti(ys, xs, ys + dy + 1, xs + dx) < 2)
		++dy;
	else if (xs + dx < xe && counti(ys, xs, ys + dy, xs + dx + 1) < 2)
		++dx;
	
	F(y, ys, ys + dy) F(x, xs, xs + dx)
		a[y][x] = lasti;

	solve(ys + dy, xs, ye, xs + dx);
	solve(ys, xs + dx, ye, xe);

}

int main(int argc, char* argv[])
{
	ifstream ins("in.txt");
    ofstream outs("out.txt");

    int T; ins >> T;
    F(t,0,T) {
		int D, N; ins >> D >> N;
		
		int K[1000], S[1000];
		F(i,0,N)
			ins >> K[i] >> S[i];
	
		double tmax = 0.;
		F(i, 0, N) {
			double t = (D - K[i]) / (double)S[i];
			tmax = max(tmax, t);
		}
		double speed = D / tmax;
	
		outs << std::setprecision(16) << "Case #" << t + 1 << ": " << speed << endl;
    }
    return 0;
}


