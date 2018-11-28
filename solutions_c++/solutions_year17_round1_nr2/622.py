#include <iostream>
#include <iomanip>
#include <sstream>
#include <vector>
#include <string>
#include <set>
#include <unordered_set>
#include <map>
#include <unordered_map>
#include <stack>
#include <queue>
#include <deque>
#include <algorithm>
#include <functional>
#include <iterator>
#include <limits>
#include <numeric>
#include <utility>
#include <type_traits>
#include <cmath>
#include <cassert>
#include <cstdio>

using namespace std;
using namespace placeholders;

using LL = long long;
using ULL = unsigned long long;
using VI = vector< int >;
using VVI = vector< vector< int > >;
using VS = vector< string >;
using ISS = istringstream;
using OSS = ostringstream;
using PII = pair< int, int >;
using VPII = vector< pair< int, int > >;
template < typename T = int > using VT = vector< T >;
template < typename T = int > using VVT = vector< vector< T > >;
template < typename T = int > using LIM = numeric_limits< T >;

template < typename T > inline istream& operator>>( istream &s, vector< T > &v ){ for ( T &t : v ) { s >> t; } return s; }
template < typename T > inline ostream& operator<<( ostream &s, const vector< T > &v ){ for ( int i = 0; i < int( v.size() ); ++i ){ s << ( " " + !i ) << v[i]; } return s; }

template < typename T > struct getv_fmt;
template <> struct getv_fmt<       int >{ static constexpr const char *fmt = "%d"; };
template <> struct getv_fmt< long long >{ static constexpr const char *fmt = "%lld"; };
template < typename T > void getv( std::vector< T > &v ){ for_each( begin( v ), end( v ), []( T &a ){ scanf( getv_fmt< T >::fmt, &a ); } ); };

template < typename T > inline T fromString( const string &s ) { T res; istringstream iss( s ); iss >> res; return res; }
template < typename T > inline string toString( const T &a ) { ostringstream oss; oss << a; return oss.str(); }

#define NUMBERED( name, number ) NUMBERED2( name, number )
#define NUMBERED2( name, number ) name ## _ ## number
#define REP1( n ) REP2( NUMBERED( REP_COUNTER, __LINE__ ), n )
#define REP2( i, n ) REP3( i, 0, n )
#define REP3( i, m, n ) for ( int i = ( int )( m ); i < ( int )( n ); ++i )
#define GET_REP( a, b, c, F, ... ) F
#define REP( ... ) GET_REP( __VA_ARGS__, REP3, REP2, REP1 )( __VA_ARGS__ )
#define FOR( e, c ) for ( auto &&e : c )
#define ALL( c ) begin( c ), end( c )
#define AALL( a ) ( remove_all_extents< decltype( a ) >::type * )a, ( remove_all_extents< decltype( a ) >::type * )a + sizeof( a ) / sizeof( remove_all_extents< decltype( a ) >::type )
#define DRANGE( c, p ) begin( c ), begin( c ) + ( p ), end( c )

#define SZ( v ) ( (int)( v ).size() )
#define EXIST( c, e ) ( ( c ).find( e ) != ( c ).end() )

template < typename T > inline bool chmin( T &a, const T &b ){ if ( b < a ) { a = b; return true; } return false; }
template < typename T > inline bool chmax( T &a, const T &b ){ if ( a < b ) { a = b; return true; } return false; }

#define PB push_back
#define EM emplace
#define EB emplace_back
#define BI back_inserter

#define MP make_pair
#define fst first
#define snd second

#define DUMP( x ) cerr << #x << " = " << ( x ) << endl

constexpr double EPS = 1e-12;

// 最大流（ Dinic 法 ） O( |E||V|^2 )
class Dinic
{
	struct Edge
	{
		int to, cap, rev;
		Edge( int t, int c, int r ) : to( t ), cap( c ), rev( r ) {}
	};

	vector< vector<Edge> > G;
	vector<int> distance, done;

public:
	Dinic( int V ) : G( V ), distance( V ), done( V )
	{
		return;
	}

	void connect( int from, int to, int cost )
	{
		G[ from ].push_back( Edge( to, cost, G[ to ].size() ) );
		G[ to ].push_back( Edge( from, 0, G[ from ].size() - 1 ) );
		return;
	}

	int solve( int s, int t )
	{
		int res = 0;
		while ( true )
		{
			bfs( s );
			if ( distance[t] < 0 )
			{
				return res;
			}

			fill( done.begin(), done.end(), 0 );
			for ( int f; ( f = dfs( s, t, numeric_limits<int>::max() ) ) > 0; res += f );
		}
	}

private:
	void bfs( int s )
	{
		fill( distance.begin(), distance.end(), -1 );
		distance[s] = 0;
		
		queue<int> que;
		que.push( s );
		while ( !que.empty() )
		{
			int v = que.front();
			que.pop();

			for ( int i = 0; i < (int)G[v].size(); ++i )
			{
				Edge &e = G[v][i];
				if ( e.cap > 0 && distance[ e.to ] < 0 )
				{
					distance[ e.to ] = distance[v] + 1;
					que.push( e.to );
				}
			}
		}

		return;
	}

	int dfs( int v, int t, int f )
	{
		if ( v == t )
		{
			return f;
		}

		for ( int &i = done[v]; i < (int)G[v].size(); ++i )
		{
			Edge &e = G[v][i];
			if ( e.cap > 0 && distance[v] < distance[ e.to ] )
			{
				int d = dfs( e.to, t, min( f, e.cap ) );
				if ( d > 0 )
				{
					e.cap -= d;
					G[ e.to ][ e.rev ].cap += d;
					return d;
				}
			}
		}

		return 0;
	}
};
// Dinic( |V| )
// connect( from, to, cap )
// solve( s, t )

int solve()
{
	int N, P;
	cin >> N >> P;

	VT< LL > R( N );
	cin >> R;

	VVT< LL > Q( N, VT< LL >( P ) );
	cin >> Q;

	Dinic maxflow( N * P * 2 + 2 );
	// [ 0, N * P ) := in
	// [ N * P, N * P * 2 ) := out
	const int SRC = N * P * 2;
	const int SINK = SRC + 1;

	const auto min_k = [&]( const int i, const int j ){ 
		int lb = 0, ub = 1'100'000;
		while ( lb + 1 < ub )
		{
			const int mid = ( lb + ub ) / 2;
			( Q[i][j] * 10 <= mid * R[i] * 11 ? ub : lb ) = mid;
		}
		return ub;
	};
	const auto max_k = [&]( const int i, const int j ){
		int lb = 0, ub = 1'100'000;
		while ( lb + 1 < ub )
		{
			const int mid = ( lb + ub ) / 2;
			( mid * R[i] * 9 <= Q[i][j] * 10 ? lb : ub ) = mid;
		}
		return lb;
	};

	const auto v_id = [&]( const int i, const int j ){ return i * P + j; };

	REP( i, N )
	{
		REP( j, P )
		{
			maxflow.connect( v_id( i, j ), N * P + v_id( i, j ), 1 );
		}
	}

	REP( j, P )
	{
		{
			const int a = min_k( 0, j ), b = max_k( 0, j );
			if ( a <= b )
			{
				maxflow.connect( SRC, v_id( 0, j ), 1 );
			}
		}
		{
			const int a = min_k( N - 1, j ), b = max_k( N - 1, j );
			if ( a <= b )
			{
				maxflow.connect( N * P + v_id( N - 1, j ), SINK, 1 );
			}
		}
	}
	REP( i, N - 1 )
	{
		REP( j, P )
		{
			REP( k, P )
			{
				const int a = min_k( i, j ), b = max_k( i, j ), c = min_k( i + 1, k ), d = max_k( i + 1, k );
				if ( max( a, c ) <= min( b, d ) )
				{
					maxflow.connect( N * P + v_id( i, j ), v_id( i + 1, k ), 1 );
				}
			}
		}
	}

	return maxflow.solve( SRC, SINK );
}

int main()
{
	cin.tie( 0 );
	ios::sync_with_stdio( false );
	cout << setprecision( 12 ) << fixed;

	int T;
	cin >> T;

	REP( i, T )
	{
		cout << "Case #" << i + 1 << ": " << solve() << endl;
	}

	return 0;
}
