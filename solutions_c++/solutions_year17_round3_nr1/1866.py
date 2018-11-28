#include <stdio.h>
#include <algorithm>
#include <vector>
#include <queue>
#include <functional>
#include <memory.h>

using namespace std;

const double PI = 3.141592653589793238;

struct Cake
{
	int H;
	int R;
	int index;

	bool operator< ( Cake& rValue )
	{
		if( this->R == rValue.R )
		{
			return this->H > rValue.H;
		}

		return this->R > rValue.R;
	}
};

int N, K;

int main()
{
	freopen( "A-large.in", "r", stdin );	
	FILE *output = fopen( "gsan.out", "w" );

	int T;
	scanf( "%d", &T );	

	Cake cake[1000];

	for( int tc = 1; tc <= T; tc++ )
	{		
		scanf( "%d %d", &N, &K );
		for( int i = 0; i < N; i++ )
		{
			scanf( "%d %d", &cake[i].R, &cake[i].H );
			cake[i].index = i;
		}

		sort( cake, cake + N );
		
		vector< pair< double, Cake* > > sideArea;
		for( int i = 0; i < N; i++ )
		{
			sideArea.push_back( pair< double, Cake* >( cake[i].H*1.0 * cake[i].R*1.0 * 2 * PI , &cake[i] ) );
		}

		sort( sideArea.begin(), sideArea.end(), greater< pair< double, Cake* > >() );

		double ans = 0;

		for( int i = 0; i <= N - K; i++ )
		{

			int R =  cake[i].R;
			int curIndex = cake[i].index;
			int k = K - 1;
			
			double tmp = cake[i].R * 1.0 * cake[i].R * 1.0 * PI + cake[i].H * 1.0 * cake[i].R * 2 * PI;

			for( int j = 0; j < N && k > 0; j++ )
			{
				if( sideArea[j].second->index != curIndex && sideArea[j].second->R <= R )
				{
					tmp += sideArea[j].first;
					k--;
				}
			}

			ans = max( ans, tmp );
		}

		printf( "Case #%d: %.9lf\n", tc, ans );

		fprintf( output, "Case #%d: %.9lf\n", tc, ans );
	}

	fclose( output );
	return 0;
}