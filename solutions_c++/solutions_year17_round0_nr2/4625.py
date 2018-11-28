#include<iostream>
#include<string>

using namespace std;

int main(){
	int kases; cin >> kases;
	for( int kase = 1; kase <= kases; kase++ ){
		string N; cin >> N;
		string res = N;
		for( int i = 1; i < int(res.length()); i++ ){
			if( res[ i ] < res[ i - 1 ] ) {
				i--;
				int j = i-1;
				while( j >= 0 && res[ i ] == res[ j ] ){ j--; }
				j++;
				if( res[ i ] == '1' ){
					res = string( int(N.length())-1, '9' );
				}
				else{
					res[ j ]--;
					for( int k = j + 1; k < int(res.length()); k++ ){
						res[ k ] = '9';
					}
				}
				
			}
		}	
		cout << "Case #" << kase <<": " << res << endl;
	}
}
