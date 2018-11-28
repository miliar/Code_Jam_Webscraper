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

const int M = 1000000007;

map<i64, int> ca;


int main(int argc, char* argv[])
{
	ifstream ins("in.txt");
    ofstream outs("out.txt");

    int T; ins >> T;
    F(t,0,T) {
		string S; ins >> S;

		int n = S.length();
		bool dirty = true;
		while( dirty ) {
			dirty = false;
			F(i, 0, n - 1) {
				if (S[i] > S[i + 1]) {	// violation
					dirty = true;
					--S[i];
					F(j, i + 1, n)
						S[j] = '9';
				}
			}
		}	// end: dirty
		while (S[0] == '0')
			S = S.substr(1);

		outs << "Case #" << t + 1 << ": " << S << endl;
    }
    return 0;
}


