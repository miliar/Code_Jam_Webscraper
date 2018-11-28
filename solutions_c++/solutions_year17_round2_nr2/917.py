#include <stdio.h>
#include <string>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#include <deque>

using namespace std;

string getCombi( int R, int O, int Y, int G, int B, int V )
{
	string resstr = "";
	int i;
	if ( R == 0 && Y == 0 && G == 0 && V == 0 && O == B ) {
		for ( i = 0; i < O; i++ ) {
			resstr += "OB";
		}
		return resstr;
	}
	if ( B == 0 && Y == 0 && O == 0 && V == 0 && G == R ) {
		for ( i = 0; i < G; i++ ) {
			resstr += "GR";
		}
		return resstr;
	}
	if ( R == 0 && O == 0 && G == 0 && B == 0 && V == Y ) {
		for ( i = 0; i < V; i++ ) {
			resstr += "YV";
		}
		return resstr;
	}

	if ( G >= R && G != 0 ) return string("IMPOSSIBLE");
	if ( O >= B && O != 0 ) return string("IMPOSSIBLE");
	if ( V >= Y && V != 0 ) return string("IMPOSSIBLE");
	
	
	R = R - G;
	Y = Y - V;
	B = B - O;

	if ( R > Y+B ) return string("IMPOSSIBLE");
	if ( Y > R+B ) return string("IMPOSSIBLE");
	if ( B > R+Y ) return string("IMPOSSIBLE");
	
	//printf( "RYB %d %d %d\n", R, Y, B );
	deque<int> avail;
	avail.push_back( R );
	avail.push_back( 0 );
	avail.push_back( Y );
	avail.push_back( 0 );
	avail.push_back( B );
	avail.push_back( 0 );
	
	deque<char> res;
	// R = 0, Y=2, B=4
	int startC;
	if ( R >= Y && R >= B ) {
		startC = 0;
		res.push_back( 'R' );
	} else if ( Y >= R && Y >= B ) {
		startC = 2;
		res.push_back( 'Y' );
	} else if ( B >= R && B >= Y ) {
		startC = 4;
		res.push_back( 'B' );
	} else {
		assert( false );
	}
	avail[startC]--;
	char colors[7] = "ROYGBV";
	int altColor[7];
	memset( altColor, 0, sizeof(altColor) );
	altColor[0] = G;
	altColor[2] = V;
	altColor[4] = O;
	
	char altColorName[7] = "G V O ";
	
	int prev = startC;
	int maxid, maxavail, maxcount;
	if ( altColor[prev] != 0 ) {
		for ( i = 0; i < altColor[prev]; i++ ) {
			res.push_back( altColorName[prev] );
			res.push_back( colors[prev] );
		}
		altColor[prev] = 0;
	}
	while ( avail[0]+avail[2]+avail[4] != 0 ) {
		maxid = -1;
		maxavail = -1;
		maxcount = 0;
		for ( i = 0; i < 6; i++ ) {
			if ( i == prev ) continue;
			if ( avail[i] == maxavail ) {
				maxcount++;
			} else if ( avail[i] > maxavail ) {
				maxid = i;
				maxavail = avail[i];
				maxcount = 1;
			}
		}
		assert( maxid != -1 );
		//printf( "m %d %d %d %d %d\n", maxid, maxavail, maxcount, startC, prev );
		if ( maxcount == 1 ) {
			assert( avail[maxid] > 0 );
			avail[maxid]--;
			res.push_back( colors[maxid] );
			prev = maxid;
		} else {
			if ( maxavail == avail[startC] && startC != prev ) {
				assert( avail[startC] > 0 );
				avail[startC]--;
				res.push_back( colors[startC] );
				prev = startC;
			} else {
				assert( avail[maxid] > 0 );
				avail[maxid]--;
				res.push_back( colors[maxid] );
				prev = maxid;
			}
		}
		if ( altColor[prev] != 0 ) {
			for ( i = 0; i < altColor[prev]; i++ ) {
				res.push_back( altColorName[prev] );
				res.push_back( colors[prev] );
			}
			altColor[prev] = 0;
		}
	}
	
	for ( i = 0; i < (int) res.size(); i++ ) {
		resstr.push_back( res[i] );
	}
	//printf( "%s\n", resstr.c_str() );
	assert( res[0] != res[res.size()-1] );
	
	return resstr;
}

int doSolve( int casenum )
{
	int N;
	int R, O, Y, G, B, V;
	scanf( " %d %d %d %d %d %d %d", &N, &R, &O, &Y, &G, &B, &V );
	
	string rval = getCombi( R, O, Y, G, B, V );
	printf( "Case #%d: %s\n", casenum, rval.c_str() );
	
	return 0;
}


int main()
{
	int cn;
	scanf( " %d", &cn );
	int i;
	for ( i = 0; i < cn; i++ ) {
		doSolve( i+1 );
	}
	return 0;
}

