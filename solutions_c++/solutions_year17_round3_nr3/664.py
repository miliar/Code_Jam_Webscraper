#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main()
{
	freopen( "C-small-1-attempt0.in", "r", stdin );
	freopen( "C-small-1-attempt0.out", "w", stdout );
	cout.precision( 10 );
	int T;
	cin >> T;
	for( int t = 1; t <= T; t++ )
	{
		unsigned int N, K;
		double U;
		cin >> N >> K >> U;
		vector<double> p( N );
		for( unsigned int i = 0; i < N; i++ )
			cin >> p[ i ];
		sort( p.begin(), p.end() );
		int i = 0;
		double s = 0, l = 1.0;
		for( i = 0; i < p.size(); i++ )
		{
			if( l <= p[ i ] )
				break;
			s += p[ i ];
			l = ( s + U ) / ( i + 1 );
		}
		for( int j = 0; j < i; j++ )
			p[ j ] = l;
		double res = 1.0;
		for( i = 0; i < p.size(); i++ )
			res *= p[ i ];
		cout << "Case #" << to_string( t ) << ": " << fixed << res << endl;
	}
	return 0;
}
