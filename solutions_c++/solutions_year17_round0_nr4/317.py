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

struct Mod {
	char c;
	int R, C;
};

int getscore( char c ) {
	if ( c == '.' )
		return 0;
	if ( c == '+' )
		return 1;
	if ( c == 'x' )
		return 1;
	if ( c == 'o' )
		return 2;
	return 0;
}

struct Stat {
	vector<int> rowx, colx, diaglx, diagrx;
	int score;
    map<int, Mod> mods;
	vector<string> stage;

	Stat( int N ) {
		stage.resize( N, string( N, '.' ) );
		rowx.resize( N, 0 ), colx.resize( N, 0 ), diaglx.resize( N + N - 1, 0 ), diagrx.resize( N + N - 1, 0 );
		score = 0;
	}

	void add( char c, int R, int C ) {
		score -= getscore( stage[R][C] );
		if ( stage[R][C] != '.' ) {
			if ( stage[R][C] != '+' ) {
				rowx[R]--;
				colx[C]--;
			}
			if ( stage[R][C] != 'x' ) {
				diaglx[stage.size() + R - C - 1]--;
				diagrx[R + C]--;
			}
		}
		stage[R][C] = c;
		score += getscore( stage[R][C] );
		if ( stage[R][C] != '.' ) {
			if ( stage[R][C] != '+' ) {
				rowx[R]++;
				colx[C]++;
			}
			if ( stage[R][C] != 'x' ) {
				diaglx[stage.size() + R - C - 1]++;
				diagrx[R + C]++;
			}
		}
	}

	bool can_place( char c, int R, int C ) {
		if ( stage[0] == "o." && stage[1] == ".." && c == 'o' ) {
			cout << ' ';
		}
		if ( c == '.' )
			return false;
		if ( stage[R][C] != '.' && c != 'o' )
			return false;
		if ( stage[R][C] == c )
			return false;
		if ( c != '+' ) {
			int isP = stage[R][C] != '.' && stage[R][C] != '+';
			int ROW = rowx[R] - isP;
			int COL = colx[C] - isP;
			if ( ROW > 0 || COL > 0 )
				return false;
		}
		if ( c != 'x' ) {
			int isX = stage[R][C] != '.' && stage[R][C] != 'x';
			int DIAGL = diaglx[stage.size() + R - C - 1] - isX;
			int DIAGR = diagrx[R + C] - isX;
			if ( DIAGL > 0 || DIAGR > 0 )
				return false;
		}
		return true;
	}
};

vector<char> chars = { '.','+','x','o' };

void solve( istream &is ){
	ofstream ofs( "output.txt" );
	int T;
	is >> T;
	for ( int tt = 1; tt <= T; ++tt ) {
		int N, M;
		is >> N >> M;
		Stat stat( N );
		while ( M-- ) {
			char c;
			int R, C;
			is >> c >> R >> C;
			--R; --C;
			stat.add( c, R, C );
		}
		ofs << "Case #" << tt << ": ";

		vector<pair<int, int>> indexes;
		for ( int i = 0; i <= N / 2; ++i ) {
			for ( int C = i; C < N - i; ++C ) {
				indexes.push_back( { i, C } );
			}
			for ( int R = i+1; R < N - i - 1; ++R ) {
				indexes.push_back( { R, N - i - 1 } );
			}
			if ( i < N / 2 )
			for ( int C = N - i - 1; C >= i; --C ) {
				indexes.push_back( { N-i-1, C } );
			}
			for ( int R = N - i - 2; R >= i+1; --R ) {
				indexes.push_back( { R, i } );
			}
		}

		for ( auto &p : indexes ) {
			int i = p.first, j = p.second;
			if ( stat.can_place( '+', i, j ) ) {
				stat.add( '+', i, j );
				stat.mods[i*N + j] = { '+', i, j };
			}
			else if ( stat.can_place( 'o', i, j ) ) {
				stat.add( 'o', i, j );
				stat.mods[i*N + j] = { 'o', i, j };
			}			
		}

		for ( auto &p : indexes ) {
		int i = p.first, j = p.second;
			if ( stat.can_place( 'x', i, j ) ) {
				stat.add( 'x', i, j );
				stat.mods[i*N + j] = { 'x', i, j };
			}
			else if ( stat.can_place( 'o', i, j ) ) {
				stat.add( 'o', i, j );
				stat.mods[i*N + j] = { 'o', i, j };
			}			
		}

		ofs << stat.score << ' ' << stat.mods.size() << '\n';
		for ( auto &p : stat.mods )
			ofs << p.second.c << ' ' << p.second.R+1 << ' ' << p.second.C+1 << '\n';
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
