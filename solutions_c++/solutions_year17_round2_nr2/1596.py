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

const int RED = 1, YELLOW = 2, BLUE = 4, ORANGE = 3, GREEN = 6, VIOLET = 5;

struct UNIC {
	int m;
	int n;
};
UNIC unics[6];


// OGVRYB
//unsigned n[6];
//unsigned m[6] = { 3,6,5,2,4,6 };
int mlast=0, mfirst=0;


int choose_next() {
	int choice = -1;
	int nchoice = -1;
	F(i, 0, 6) {
		if (unics[i].m & mlast)	// conflict
			continue;
		if (unics[i].n == 0)
			continue;
		if (unics[i].n > nchoice) {	// maxn
			choice = i;
			nchoice = unics[i].n;
		}
		else if (unics[i].n == nchoice && (unics[i].m & mfirst)) {	// resolve ties to avoid collisions with first
			choice = i;
			nchoice = unics[i].n;
		}
	}
	if (choice == -1)
		return choice;
	mlast = unics[choice].m;
	--unics[choice].n;
	if (!mfirst)
		mfirst = mlast;
	return choice;
}


int main(int argc, char* argv[])
{
	ifstream ins("in.txt");
    ofstream outs("out.txt");

    int T; ins >> T;
    F(t,0,T) {
		mlast = mfirst = 0;
		int N,R,O,Y,G,B,V; ins >> N >> R >> O >> Y >> G >> B >> V;
		unics[0].m = ORANGE;
		unics[0].n = O;
		unics[1].m = GREEN;
		unics[1].n = G;
		unics[2].m = VIOLET;
		unics[2].n = V;
		unics[3].m = RED;
		unics[3].n = R;
		unics[4].m = YELLOW;
		unics[4].n = Y;
		unics[5].m = BLUE;
		unics[5].n = B;

		string ret;
		char chara[] = "OGVRYB";

		int ch;
		while ((ch = choose_next()) != -1) {
			ret += chara[ch];
		}

		/*int first = 0, last = 0, *pch;
		do {
			if( !(last & ORANGE) )
				pch = &O;
			if (G > *pch) pch = &G;
			if (V > *pch) pch = &V;
			if (R > *pch) pch = &R;
			if (Y > *pch) pch = &Y;
			if (B > *pch) pch = &B;
			last = *pch;
			if (!first)
				first = last;
		} while( *pch > 0 )*/
		if( ret.length() != N || (mlast & mfirst) )
			outs << "Case #" << t + 1 << ": " << "IMPOSSIBLE" << endl;
		else
			outs << "Case #" << t + 1 << ": " << ret << endl;
    }
    return 0;
}


