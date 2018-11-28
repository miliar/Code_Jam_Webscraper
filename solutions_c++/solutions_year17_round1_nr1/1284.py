#include<iostream>
#include<string>
#include<set>
using namespace std;

char A[ 30 ][ 30 ];
int bfs[ 3000 ];
int mx[ 4 ] = { 0 , 0, 1, -1 };
int my[ 4 ] = { -1, 1, 0, 0 };

int I[ 300 ];

int main(){
	int T; cin >> T;	
	for( int kase = 1; kase <= T; kase++ ){
		cout << "Case #" << kase << ":" << endl;
		int R, C; cin >> R >> C;
		int p = 0, t = 0;
		for( int r = 0; r < R; r++ )
			for( int c = 0; c < C; c++ ){
				cin >> A[ r ][ c ];
				if( A[ r ][ c ] == '?' ) t++;
				/*if( A[ r ][ c ] != '?' ){
					bfs[ t++ ] = r; bfs[ t++ ] = c;
				}*/
			}
		set< char > used;
		while( t ){
			int maxi = 0; char ac, acres;
			int fr, tr, fc, tc;
			for( int r = 0; r < R; r++ ){	
				for( int c = 0; c < C; c++ ){
					for( int r2 = r; r2 < R; r2++ ){
						for( int c2 = c; c2 < C; c2++ ){
							set< char > sc;
							for( int i = r; i <= r2; i++ ){
								for( int j = c; j <= c2; j++ ){
									if( A[ i ][ j ] != '?' ){
										sc.insert( A[ i ][ j ] ); ac = A[ i ][ j ];
									}
								}
							}
							if( sc.size() == 1u && (r2-r+1)*(c2-c+1) > maxi && used.find( ac ) == used.end() ){
								maxi = (r2-r+1)*(c2-c+1); //used.insert( ac );
								fr = r; tr = r2; fc = c; tc = c2; acres = ac;
							}
						}
					}
				}
			}		
			if( maxi > 0 ){
				used.insert( acres );
				for( int i = fr; i <= tr; i++ ){	
					for( int j = fc; j <= tc; j++ ){
						A[ i ][ j ] = acres;
					}
				}
			}
			t = 0;
			for( int i = 0; i < R; i++ ){
				for( int j = 0; j < C; j++ ){
					t += (A[i][j] == '?');
				}
			}
		}
		for( int r = 0; r < R; r++ ){
			for( int c = 0; c < C; c++ ){
				cout << A[ r ][ c ];
			}cout << endl;
		}
	}
}
