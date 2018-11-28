#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <map>
#include <set>
#include <unordered_set>
#include <unordered_map>
#include <utility>
#include <string>
#include <cstring>
#include <queue>
#include <stack>

#define DBGMODE
#ifdef DBGMODE
#  include <intrin.h>
#  define __builtin_popcount __popcnt
#endif

#define NMAX 1000000000000000000ULL
#define MOD 1000000009

#define DEBUG(x) cout << '>' << #x << ": " << x << endl;
inline bool EQ( double a, double b ) { return fabs( a - b ) < 1e-9; }

using namespace std;

typedef unsigned long long ULL;
typedef long long LL;

inline int two( int n ) { return 1 << n; }
inline int test( int n, int b ) { return ( n >> b ) & 1; }
inline void set_bit( int & n, int b ) { n |= two( b ); }
inline void unset_bit( int & n, int b ) { n &= ~two( b ); }
inline int last_bit( int n ) { return n & ( -n ); }
inline int ones( int n ) { return __builtin_popcount( n ); }

template<class T> void chmax( T & a, const T & b ) { a = max( a, b ); }
template<class T> void chmin( T & a, const T & b ) { a = min( a, b ); }
///////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Mit nezel Jozsi? :D

ULL pow10( int i ) {
	ULL res = 1;
	while ( i-- ) {
		res *= 10;
	}
	return res;
}

int getdigit( ULL n, int i ) {
	return ( n / pow10( i ) ) % 10;
}

void solve( istream &is ){
	ofstream ofs( "output.txt" );
	int T;
	is >> T;
	for ( int tt = 1; tt <= T; ++tt ) {
		ULL N;
		is >> N;
		ULL nc = N;
		int digits = 0;
		while ( nc ) {
			nc /= 10;
			digits++;
		}
		for ( int i = digits - 1; i > 0; --i ) {
			int left = getdigit( N, i );
			int right = getdigit( N, i-1 );
			if ( left > right ) {
				N = N - ( N % pow10( i ) );
				--N;
				i = digits;
			}
		}
		ofs << "Case #" << tt << ": ";
		ofs << N << '\n';
	}
}

int main() {
	ios::sync_with_stdio( false );
	cin.tie( nullptr );
	cout.tie( nullptr );

#ifdef DBGMODE
	ifstream ifs( "input.txt" );
	solve( ifs );
	int n__;
	cin >> n__;
#else
	solve( cin );
#endif

	return 0;
}
