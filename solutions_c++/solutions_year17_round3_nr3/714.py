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
		int N, K;
		cin >> N >> K;
		double U; cin >> U;
		vector< double > vd( N );
		for( int n = 0; n < N; n++ ) cin >> vd[ n ];
		sort( vd.begin(), vd.end() );
		double res = 0.0;
		for( int i = 0; i < N; i++ ) 
			res += vd[ i ];
		res += U;
		if( res >= N ) res = 1.0;
		else{
			res /= double( N );
			int r = -1;
			for( int i = 0; i < N; i++ ){
				if( vd[ i ] > res ){ 
					r = i;
					break;
				}
			}
			if( r == -1 ) r = N;
			double res2 = U;
			for( int i = 0; i < r; i++ ){
				res2 += vd[ i ];
			}
			res2 /= double(r);
			for( int i = 0; i < r; i++ ) vd[ i ] = res2;
			res = 1.0;
			for( int k = N-K; k < N; k++ ){
				res *= vd[ k ];
			}
		}
		/*int prev = 0;
		for( int k = N-K; k < N; k++ ){
			if( k + 1 == N ){
				if( prev == 0 )
					vd[ k ] = min( vd[ k ] + U, 1.0 );
				else{
					for( int k2 = N-prev; k2 < N; k2++ )
						vd[ k2 ] = min( vd[ k2 ] + U/double(prev), 1.0 );
				}
			}
			else if( vd[ k ] == vd[ k + 1 ] ){
				prev++;
			}
			else if( prev == 0 ){
				if( vd[ k ] + U <= vd[ k + 1 ] ){
					vd[ k ] += U; break;
				}
				U -= (vd[k+1]-vd[k]);
				vd[ k ] = vd[ k + 1 ];
				prev++;
			}
			else{
				if( vd[ k ] + U/double(prev) <= vd[ k + 1 ] ){
					for( int k2 = k-prev; k2 <= k; k2++ )
						vd[ k2 ] += (U/double(prev));
					break;
				}
				U -= ((vd[k+1]-vd[k])*prev);
				for( int k2 = k-prev; k2 <= k; k2++ )
					vd[ k2 ] = vd[ k+1 ];
				prev++;
			}
		}*/
		cout << "Case #" << kase <<": " << res << endl;	
	}
}
