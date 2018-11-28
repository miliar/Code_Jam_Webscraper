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

#define NMAX 1000000000
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

set<int> getServing( int gram, int req ){
	set<int> servings;
	int lower = gram / 1.1;
	lower = lower / req * req;
	int upper = gram / 0.9;
	upper = ( upper / req + 1 ) * req;
	for ( int i = lower; i <= upper; i += req ) {
		if ( abs( i - gram ) <= i*0.1 )
			servings.insert( i / req );
	}
	if ( servings.empty() )
		servings.insert( 0 );
	return servings;
}

void solve( istream &is ){
	ofstream ofs( "output.txt" );
	int T;
	is >> T;
	for ( int tt = 1; tt <= T; ++tt ) {
		int N, P;
		is >> N >> P;
		vector<int> recipe( N );
		vector<vector<int>> packages( N, vector<int>( P ) );
		for ( int i = 0; i < N; ++i ) {
			is >> recipe[i];
		}
		for ( int i = 0; i < N; ++i ) {
			for ( int j = 0; j < P; ++j ) {
				is >> packages[i][j];
			}
		}
		for ( auto &v : packages ) {
			sort( v.begin(), v.end() );
		}
		int num = 0;

		vector<int> indexes( N, 0 );
		while ( all_of( indexes.begin(), indexes.end(), [&]( int i ){ return i < P; } ) ) {
			map<int, int> serv;
			vector<set<int>> servings;
			for ( int i = 0; i < N; ++i ) {
				servings.push_back( getServing( packages[i][indexes[i]], recipe[i] ) );
				for ( int s : servings.back() )
					serv[s]++;
			}
			int serving = -1;
			int minval = 10000000;
			for ( auto &p : serv ) {
				if ( p.second == N )
					serving = p.first;
				chmin( minval, p.first );
			}
			if ( serving <= 0 ) {
				int minindex = -1;
				for ( int i = 0; i < N; ++i ) {
					int imin = *min_element( servings[i].begin(), servings[i].end() );
					if ( imin == minval && ( minindex == -1 || servings[i].size() < servings[minindex].size() ) )
						minindex = i;
				}
				indexes[minindex]++;
			}
			else {
				++num;
				for ( int &i : indexes )
					++i;
			}
		}
		ofs << "Case #" << tt << ": ";
		ofs << num << '\n';
	}
}

int main() {
	ios::sync_with_stdio( false );
	cin.tie( nullptr );
	cout.tie( nullptr );

#ifdef DBGMODE
	ifstream ifs( "input.txt" );
	solve( ifs );
#else
	solve( cin );
#endif

	return 0;
}
