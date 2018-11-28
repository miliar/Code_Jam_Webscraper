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

VS solve()
{
	int H, W;
	cin >> H >> W;

	VS board( H );
	cin >> board;

	const auto is_empty = []( const string &row ){ return all_of( ALL( row ), bind( equal_to< char >(), _1, '?' ) ); };

	string prev;
	FOR( row, board )
	{
		if ( !is_empty( row ) )
		{
			prev = row;

			char p = '?';
			FOR( c, prev )
			{
				if ( c != '?' )
				{
					p = c;
				}
				c = p;
			}

			const auto it = find_if( ALL( prev ), bind( not_equal_to< char >(), _1, '?' ) );
			fill( begin( prev ), it, *it );
		}

		row = prev;
	}

	const auto it = find_if_not( ALL( board ), is_empty );
	fill( begin( board ), it, *it );

	return move( board );
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
		const VS res = solve();
		cout << "Case #" << i + 1 << ": \n";
		copy( ALL( res ), ostream_iterator< string >( cout, "\n" ) );
	}
	cout << flush;

	return 0;
}
