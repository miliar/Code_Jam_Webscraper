#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
using namespace std;


int main(){
	int T; cin >> T;
	for( int kase = 1; kase <= T; kase++ ){
		long long N, K;
		cin >> N >> K;
		long long c = 1;
		//long long vo = 0, ve = 0;
		//long long qo = 0, qe = 0;
		long long res1, res2;
		/*if( N & 1 ){
			vo = N;
			qo = 1;
		}
		else{
			ve = N;
			qe = 1;
		}*/
		vector< int > val;
		val.push_back( N );
		while( K ){
			//for( int i = 0; i < int(val.size()); i++ ) cout << " " << val[ i ]; cout << endl;
			if( c > K ){
				res1 = val[ int(val.size()) - K ];
				res2 = val[ int(val.size()) - K ];
				if( res1 & 1 ){
					res1 /= 2; res2 /= 2;	
				}
				else{
					res1 /= 2; res2 = (res2-1)/2;
				}
				break;
			}
			K -= c;
			c *= 2;
			vector< int > aux;
			for( int i = 0; i < int(val.size()); i++ ){
				if( val[ i ]& 1 ){
					aux.push_back( val[ i ]/2 ); aux.push_back( val[ i ]/2 );
					if( i == 0 ){
						res1 = res2 = val[ i ] / 2;
					}
				}
				else{
					aux.push_back( val[ i ]/2 ); aux.push_back( (val[ i ]-1)/2 );
					if( i == 0 ){
						res1 = val[ i ] / 2;
						res2 = ( val[ i ] - 1 ) / 2;
					}
				}
			}
			sort( aux.begin(), aux.end() );
			val = aux;
			//for( int i = 0; i < int(aux.size()); i++ ) cout << " " << aux[ i ]; cout << endl;
			
			/*if( c > K ){
				if( qe == 0 ){
					res1 = vo/2;
					res2 = vo/2;
				}
				else if( qo == 0 ){
					res1 = ve/2;
					res2 = max((ve/2)-1,0LL);
				}
				else if( vo > ve ){
					if( K < qo ){
						res1 = vo;
						res2 = vo/2;
					}
					else if( K == qo ){
						res1 = ve;
						res2 = vo/2;
					}
					else{
						res1 = ve;
						res2 = (ve/2)-1;
					}
				}
				else{
					if( K < qe ){
						res1 = ve;
						res2 = max((ve/2)-1,0LL);
					}
					else if( K == qe ){
						res1 = vo;
						res2 = (ve/2)-1;
					}
					else{
						res1 = vo;
						res2 = vo/2;
					}
				}
				break;
			}
			K -= c;
			c *= 2;
			long long a1, a3, a4;
			long long ao = 0, ae = 0;
			a1 = (vo/2);
			a3 = (ve/2);
			a4 = max((ve/2)-1,0LL);
			vo = ve = 0;
			if( a1 & 1 ){ vo = a1; ao += 2*qo; }
			else{ ve = a1; ae += 2*qo;}
			if( a3 & 1 ){ vo = a3; ao += qe; }
			else{ ve = a3; ae += qe; }
			if( a4 & 1 ){ vo = a4; ao += qe; }
			else{ ve = a4; ae += qe; }
			qo = ao; qe = ae;
			cout << "(" << vo << "," << ve << ") <=> (" << qo << "," << qe << ")" << endl;
			res1 = max( vo, ve ); res2 = min( vo, ve );*/
				
		}
		cout << "Case #" << kase << ": " << res1 << " " << res2 << endl;
		
	}
}
