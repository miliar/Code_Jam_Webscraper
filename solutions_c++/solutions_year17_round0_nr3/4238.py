/*
 * source.cpp
 *
 *  Created on: Apr 8, 2017
 *      Author: tigran
 */



#include <iostream>
#include <algorithm>
#include <vector>
#include <list>
#include <cassert>

using namespace std;

typedef list< long long > gaps_type;
typedef typename gaps_type::iterator gaps_it_type;

void find_max_positions( gaps_type& data, vector< gaps_it_type >& ps )
{
	ps.clear();
	int max_value = -1;
	for ( gaps_it_type it = data.begin(); it != data.end(); ++it ) {
		if ( *it > max_value ) {
			ps.clear();
			max_value = *it;
		}
		if ( *it == max_value ) {
			ps.push_back( it );
		}
	}
}


void solve()
{
	long long N, K;
	cin >> N >> K;
	gaps_type gaps;
	gaps.push_back( N );
	vector< gaps_it_type > max_indices;
	long long entered_count = 0;
	while ( true ) {
		find_max_positions( gaps, max_indices );
		for ( int i = 0; i < (int)max_indices.size(); ++i ) {
			int rem1, rem2;
			rem1 = (*(max_indices[ i ]) - 1) / 2;
			rem2 = *(max_indices[ i ]) - 1 - rem1;
			assert( rem1 <= rem2 );
			gaps.insert( max_indices[ i ], rem1 );
			gaps.insert( max_indices[ i ], rem2 );
			gaps.erase( max_indices[ i ] );
			++entered_count;
			if ( entered_count == K ) {
				cout << max( rem1, rem2 ) << " " << min( rem1, rem2 );
				return;
			}
		}
	}
}


int main()
{
	int T;
	cin >> T;
	for ( int t = 1; t <= T; ++t ) {
		cout << "Case #" << t << ": ";
		solve();
		cout << endl;
	}
	return 0;
}
