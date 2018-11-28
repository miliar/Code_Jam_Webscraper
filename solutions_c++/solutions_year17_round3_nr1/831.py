#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

struct PanCake
{
	double r;
	double h;

	bool operator <( const PanCake& other )
	{
		if( this->r == other.r )
			return this->h > other.h;
		return this->r > other.r;
	}
};

int main()
{
	freopen( "A-large.in", "r", stdin );
	freopen( "A-large.out", "w", stdout );
	cout.precision( 10 );
	int T;
	cin >> T;
	for( int t = 1; t <= T; t++ )
	{
		unsigned int N, K;
		cin >> N >> K;
		vector<PanCake> p( N );
		for( unsigned int i = 0; i < N; i++ )
			cin >> p[ i ].r >> p[ i ].h;
		sort( p.begin(), p.end() );
		vector< vector<double>> s{ K, vector<double>( N ) };
		for( unsigned int i = 0; i < N; i++ )
			s[ 0 ][ i ] = p[ i ].r * p[ i ].r + 2 * p[ i ].r * p[ i ].h;
		for( unsigned int j = 1; j < K; j++ )
		{
			double maxArea = 0;
			for( unsigned int i = j; i < N; i++ )
			{
				maxArea = max( maxArea, s[ j - 1 ][ i - 1 ] );
				s[ j ][ i ] = maxArea + 2 * p[ i ].r * p[ i ].h;
			}
		}
		double resArea = 0;
		for( unsigned int i = 0; i < N; i++ )
			resArea = max( resArea, s[ K - 1 ][ i ] );
		double resAreaDbl = resArea * acos( -1.0 );
		cout << "Case #" << to_string( t ) << ": " << fixed << resAreaDbl << endl;
	}
	return 0;
}
