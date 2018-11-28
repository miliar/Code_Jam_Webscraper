#include<string>
#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

#define PB push_back
#define MP make_pair
#define X first
#define Y second


//R + O + Y + G + B + V = N

int C[ 6 ];
int N;
string A;
bool finished;
char P[ 6 ] = {'R','O','Y','G','B','V'};


bool valid( char a, char b ){
	if( a == b ) return false;
	if( a == 'R' && (b == 'B' || b == 'Y' || b == 'G')) return true;
	if( a == 'B' && (b == 'R' || b == 'Y' || b == 'O')) return true;
	if( a == 'Y' && (b == 'R' || b == 'B' || b == 'V')) return true;
	if( a == 'O' && b == 'B') return true;
	if( a == 'G' && b == 'R') return true;
	if( a == 'V' && b == 'Y') return true;
	return false;
}

void recur( int n ){
	//cout << "N: " << n << "/"<< N << " " << A << endl;
	/*if( n == N ){
		cout << A << endl;
		finished = true;
		return;
	}
	for( int i = 0; !finished && i < 6; i++ ){
		if( C[ i ] > 0 && 
			valid( A[ n - 1 ], P[ i ] ) && 
			( n + 1 < N || 
				( n + 1 == N && valid( P[ i ], A[ 0 ] ) ) 
			) ){
			A[ n ] = P[ i ]; 
			C[ i ]--;
			recur( n+1 );
			C[ i ]++;
		}
	}*/
}

bool check(){
	if( C[ 5 ] == C[ 2 ] && C[ 5 ] + C[ 2 ] == N ) return true;
	if( C[ 1 ] == C[ 4 ] && C[ 1 ] + C[ 4 ] == N ) return true;
	if( C[ 3 ] == C[ 0 ] && C[ 3 ] + C[ 0 ] == N ) return true;
	if( C[ 0 ] > 0 && C[ 0 ] > (C[4]+C[2]+C[3]) ) return false;
	if( C[ 1 ] > 0 && C[ 1 ] >= (C[4])) return false;
	if( C[ 2 ] > 0 && C[ 2 ] > (C[0]+C[4]+C[5] ) )return false;
	if( C[ 3 ] > 0 && C[ 3 ] >= (C[0] ) )return false;
	if( C[ 4 ] > 0 && C[ 4 ] > (C[0]+C[2]+C[1] ) )return false;
	if( C[ 5 ] > 0 && C[ 5 ] >= C[2] )return false;
	return true;
}

int main(){
	int T; cin >> T;
	for( int kase = 1; kase <= T; kase++ ){
		cin >> N;
		for( int i = 0; i < 6; i++ ){
			cin >> C[ i ];			
		}
		A = "";
		bool possible = check();
		if( possible ){
			cout << "Case #" << kase <<": ";
			finished = true;
			string bob = "", rgr = "", yvy = "";
			while( C[ 3 ]-- ){
				rgr += "RG";
				C[ 0 ]--;
			}
			if( rgr.length() > 0u && C[ 0 ] ){ rgr += "R"; }
			else if( rgr.length() ) C[ 0 ]++;
			while( C[ 5 ]-- ){
				yvy += "YV";
				C[ 2 ]--;
			}
			if( yvy.length() > 0u && C[ 2 ] ){ yvy += "Y"; }
			else if( yvy.length() ) C[ 2 ]++;
			while( C[ 1 ]-- ){
				bob += "BO";
				C[ 4 ]--;
			}
			if( bob.length() > 0u && C[ 4 ] ){ bob += "B"; }
			else if( bob.length() ) C[ 4 ]++;
			//cout << rgr << " " << yvy << " " << bob << endl;
			A = string( C[ 0 ] + C[ 2 ] + C[ 4 ], ' ' );
			vector<pair< int, char > > vp;
			vp.PB( MP( C[ 0 ], 'R' ) );
			vp.PB( MP( C[ 2 ], 'Y' ) );
			vp.PB( MP( C[ 4 ], 'B' ) );
			sort( vp.rbegin(), vp.rend() );
			int p = 0;
			while( vp[ 0 ].X-- ){
				A[ p ] = vp[ 0 ].Y;
				p += 2;
			}
			p--;
			while( vp[ 1 ].X-- ){
				A[ p ] = vp[ 1 ].Y;
				p += 2;
				if( p >= A.length() ) p = 1;
			}
			for( int i = 0; i < int(A.length()); i++ ) 
				if( A[ i ] == ' ' ) 
					A[ i ] = vp[ 2 ].Y;
			//cout << A << endl;
			
			if( !finished || (A.length() > 1 && !valid(A[ 0 ], A[ A.length()-1u ] ) ) ) cout << "IMPOSSIBLE" << endl;
			//if( !finished ) cout << "IMPOSSIBLE" << endl;
			else{
				if( rgr.length() ){
					for( int i = 0; i < A.length(); i++ ){
						if( A[ i ] == 'R' ){
							A = A.substr( 0, i ) + rgr + A.substr( i+1 ); break;
						}
					}
				}
				if( bob.length() ){
					for( int i = 0; i < A.length(); i++ ){
						if( A[ i ] == 'B' ){
							A = A.substr( 0, i ) + bob + A.substr( i+1 ); break;
						}
					}
				}
				if( yvy.length() ){
					for( int i = 0; i < A.length(); i++ ){
						if( A[ i ] == 'Y' ){
							A = A.substr( 0, i ) + yvy + A.substr( i+1 ); break;
						}
					}
				}
				cout << A << endl;
			}
		}		
		else{
			cout << "Case #" << kase <<": IMPOSSIBLE" << endl;			
		}
	}
}
