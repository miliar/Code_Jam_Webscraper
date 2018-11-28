/*
 * C.cpp
 *
 *  Created on: Apr 22, 2017
 *      Author: tigran
 */


#include <iostream>
#include <iomanip>
#include <vector>
#include <limits>

using namespace std;


void solve()
{
	int N, Q;
	cin >> N >> Q;
	vector< long long > E( N + 1 );
	vector< long long > S( N + 1 );
	for ( int i = 1; i <= N; ++i )
		cin >> E[ i ] >> S[ i ];
	vector< vector< long long > > D(
			N + 1,
			vector< long long >( N + 1, 0 ) );
	for ( int i = 1; i <= N; ++i )
		for ( int j = 1; j <= N; ++j )
			cin >> D[ i ][ j ];

	auto dist = D;
	const long long LL_MAX = std::numeric_limits< long long >::max() / 10;
	for ( int i = 1; i <= N; ++i ) {
		for ( int j = 1; j <= N; ++j ) {
			if ( dist[ i ][ j ] == -1 )
				dist[ i ][ j ] = LL_MAX;
		}
	}
	for ( int k = 1; k <= N; ++k ) {
		for ( int i = 1; i <= N; ++i ) {
			for ( int j = 1; j <= N; ++j ) {
				dist[ i ][ j ] = min(
						dist[ i ][ j ],
						dist[ i ][ k ] + dist[ k ][ j ] );
			}
		}
	}
	for ( int i = 1; i <= N; ++i )
		dist[ i ][ i ] = LL_MAX;

	const long double LD_MAX = std::numeric_limits< long double >::max() / 1000;
	vector< vector< long double > > times(
			N + 1,
			vector< long double >( N + 1 ) );
	for ( int i = 1; i <= N; ++i ) {
		for ( int j = 1; j <= N; ++j ) {
			if ( dist[ i ][ j ] <= E[ i ] )
				times[ i ][ j ] = dist[ i ][ j ] / ((long double)S[ i ]);
			else
				times[ i ][ j ] = LD_MAX;
		}
	}
	for ( int i = 1; i <= N; ++i )
		times[ i ][ i ] = LD_MAX;

	auto c_times = times;
	for ( int k = 1; k <= N; ++k )
		for ( int i = 1; i <= N; ++i )
			for ( int j = 1; j <= N; ++j )
				c_times[ i ][ j ] = min(
						c_times[ i ][ j ],
						c_times[ i ][ k ] + c_times[ k ][ j ] );

	for ( int q = 1; q <= Q; ++q ) {
		int u, v;
		cin >> u >> v;
		cout << " " << setiosflags( ios::fixed | ios::showpoint ) << setprecision( 10 )
				<< c_times[ u ][ v ];
	}
}


int main()
{
	int tc;
	cin >> tc;
	for ( int t = 1; t <= tc; ++t ) {
		cout << "Case #" << t << ":";
		solve();
		cout << endl;
	}
	return 0;
}
