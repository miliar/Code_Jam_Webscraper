#include<bits/stdc++.h>

using namespace std;

#define X first
#define Y second
#define PB push_back
#define MP make_pair

int main(){
	cout.setf( ios::fixed );
	cout.precision( 8 );
	int T; cin >> T;
	for( int kase = 1; kase <= T; kase++ ){
		int N, K, r, h;
		cin >> N >> K;
		vector< pair< int, int > > vp;
		for( int n = 0; n < N; n++ ){
			cin >> r >> h;
			vp.PB( MP( r, h ) );
		}
		sort( vp.begin(), vp.end() );

		vector< bool > used( N, false );
		used[ 0 ] = true;

		long double resR = M_PI * vp[ 0 ].X * vp[ 0 ].X;
		long double resH = 2.0 * M_PI * vp[ 0 ].X * vp[ 0 ].Y;

		for( int i = 1; i < K; i++ ){
			resR = (M_PI * vp[ i ].X *vp[ i ].X);
			resH += (2.0 * M_PI * vp[ i ].X * vp[ i ].Y );
			used[ i ] = true;
		}

		for( int k = K; k < N; k++ ){
			long double bestR = 0.0;
			long double bestH = 0.0;
			int p = -1;
			for( int i = 0; i < k; i++ ){
				if( used[ i ] ){
					long double acR = M_PI * vp[ k ].X * vp[ k ].X-resR;
					long double acH = (2.0 * M_PI * vp[ k ].X * vp[ k ].Y ) - (2.0 * M_PI * vp[ i ].X * vp[ i ].Y );
					if( acR + acH > bestR + bestH ){
						p = i; //cout << k << " improves " << i << " " << acR << " " << acH << endl;
						bestR = acR;
						bestH = acH;
					}
				}
			}
			if( p != -1 ){
				//cout << "SWAP " << p << " " << k << endl;
				used[ p ] = false;
				used[ k ] = true;
				resR = M_PI * vp[ k ].X * vp[ k ].X; 
				resH += bestH;
			}
		}
		cout << "Case #" << kase <<": " << (resR + resH) << endl;	
	}
}
