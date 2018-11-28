/*
 * A.cpp
 *
 *  Created on: Apr 22, 2017
 *      Author: tigran
 */


#include <iostream>
#include <algorithm>
#include <iomanip>
#include <vector>

using namespace std;


void solve()
{
	long long D;
	int N;
	cin >> D >> N;
	vector< pair< long long, long long > > K_S( N );
	for ( int i = 0; i < N; ++i ) {
		cin >> K_S[ i ].first >> K_S[ i ].second;
	}
	std::sort( K_S.begin(), K_S.end() );
	double t = 0;
	for ( int i = N - 1; i >= 0; --i ) {
		double ti = (double)(D - K_S[ i ].first) / K_S[ i ].second;
		t = max( t, ti );
	}
	double v = D / t;
	cout << setiosflags( ios::fixed | ios::showpoint ) << setprecision( 12 ) << v;
}


int main()
{
	int tc;
	cin >> tc;
	for ( int t = 1; t <= tc; ++t ) {
		cout << "Case #" << t << ": ";
		solve();
		cout << endl;
	}
	return 0;
}
