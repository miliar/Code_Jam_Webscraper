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



int main(int argc, char* argv[])
{
	ifstream ins("in.txt");
    ofstream outs("out.txt");

    int T; ins >> T;
    F(t,0,T) {
		int N, K; ins >> N >> K;
		double U; ins >> U;
		double P[50];
		//int p[50];
		F(i, 0, N) {
			ins >> P[i];
			//p[i] = (int)(P[i] * 10000 + EPS);
		}

		//int u = (int)(U * 10000 + EPS);

		while ( U > EPS ) {
			sort(P, P + N);
			int nmin = 1;
			while ( nmin < N && P[nmin] - P[0] < EPS)
				++nmin;
			
			if (nmin == N) {
				F(i, 0, N)
					P[i] += U / N;
				break;
			}
			
			double dist = P[nmin] - P[0];
			double req = nmin * dist;
			if (req < U) {
				U -= req;
				F(i, 0, nmin)
					P[i] += dist;
			}
			else {
				F(i, 0, nmin)
					P[i] += U / nmin;
				U = 0.;
			}
		}
		
		
		/*F(i, 0, u) {
			sort(p, p + N);
			++p[0];
		}*/
		double res = P[0];	// p[0] / 10000.;
		F(i, 1, N)
			res *= P[i];	// (p[i] / 10000.);

		outs << std::setprecision(32) << "Case #" << t + 1 << ": " << res << endl;
    }
    return 0;
}


