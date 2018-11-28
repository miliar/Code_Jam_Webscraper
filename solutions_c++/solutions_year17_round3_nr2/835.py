#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main()
{
	freopen( "B-small-attempt0.in", "r", stdin );
	freopen( "B-small-attempt0.out", "w", stdout );
	cout.precision( 10 );
	int T;
	cin >> T;
	for( int t = 1; t <= T; t++ )
	{
		unsigned int c, j;
		cin >> c >> j;
		vector<pair< int, int>> ac( c ), aj( j );
		for( unsigned int i = 0; i < c; i++ )
			cin >> ac[ i ].first >> ac[ i ].second;
		for( unsigned int i = 0; i < j; i++ )
			cin >> aj[ i ].first >> aj[ i ].second;
		int r = 2;
		if( ac.size() > 1 || aj.size() > 1 )
		{
			vector<pair< int, int>>& b = ac.size() == 2 ? ac : aj;
			if( ( ( 1440 + b[ 0 ].second - b[ 1 ].first ) % 1440 > 720 ) &&
				( ( 1440 + b[ 1 ].second - b[ 0 ].first ) % 1440 > 720 ) )
				r = 4;
		}
		cout << "Case #" << to_string( t ) << ": " << fixed << r << endl;
	}
	return 0;
}
