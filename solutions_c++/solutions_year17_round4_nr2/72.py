#include <iostream>
#include <memory.h>
#define P pair< bool, int >
using namespace std;

int N, C, M;
int num[2000][2000];

P check( int val ){
	int rem = 0;
	int pm = 0;
	for( int i = 0; i < N; i++ ){
		int need = 0;
		for( int j = 0; j < C; j++ )
			need += num[j][i];
		if( val + rem < need )
			return P( false, 0 );
		if( need <= val ){
			rem += val - need;
		}
		else {
			pm += ( need - val );
			rem -= ( need - val );
		}
	}
	return P( true, pm );
}

int deg[2000];

int main()
{
	int test;
	cin >> test;
	for( int T = 1; T <= test; T++ ){
		memset( num, 0, sizeof num );
		memset( deg, 0, sizeof deg );
		cin >> N >> C >> M;
		int k = 0;
		for( int i = 0; i < M; i++ ){
			int p, b;
			cin >> p >> b;
			num[b - 1][p - 1]++;
			deg[b - 1] ++;
			k = max( k, deg[b - 1] );
		}
		int l = k, r = M, res = -1, pm = 0;
		while( l <= r ){
			int mid = ( l + r ) / 2;
			P ch = check( mid );
			if( ch.first == false )
				l = mid + 1;
			else{
				res = mid;
				pm = ch.second;
				r = mid - 1;
			}
		}
		cout << "Case #" << T << ": " << res << ' ' << pm << endl;
	}
	return 0;
}