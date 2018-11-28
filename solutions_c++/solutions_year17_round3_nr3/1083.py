/*
 * C.cpp
 *
 *  Created on: Apr 30, 2017
 *      Author: tigran
 */



#include <iostream>
#include <iomanip>
#include <vector>
#include <algorithm>
#include <functional>
#include <cmath>

using namespace std;


const double EPS = 1e-20;


bool equal( double a, double b )
{
	return fabs( a - b ) <= EPS;
}


double calculate_prob( const vector< double >& p, int N )
{
	double result = 1.0;
	for ( int i = 0; i < N; ++i )
		result *= p[ i ];
	return result;
}


void solve()
{
	int N, K;
	cin >> N >> K;
	double U;
	cin >> U;
	vector< double > p( N );
	for ( int i = 0; i < N; ++i )
		cin >> p[ i ];
	sort( p.begin(), p.end() );
	p.push_back( 1 );
	for ( int i = 1; i <= N; ++i ) {
		if ( equal( U, 0.0 ) )
			break;
		double dh = p[ i ] - p[ i - 1 ];
		double du = dh * i;
		if ( du > U ) {
			du = U;
			dh = du / i;
		}
		// increasing up to p[i]
		for ( int j = 0; j < i; ++j )
			p[ j ] += dh;
		// subtract from U
		U -= du;
	}
	double prob = calculate_prob( p, N );
	cout << setiosflags( ios::fixed | ios::showpoint ) << setprecision( 10 ) << prob << endl;
}


int main()
{
	int TC;
	cin >> TC;
	for ( int tc = 1; tc <= TC; ++tc ) {
		cout << "Case #" << tc << ": ";
		solve();
	}
	return 0;
}

