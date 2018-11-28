#include<iostream>
using namespace std;
string s;
int n , k ;
int main(){
	ios::sync_with_stdio(0);
	int t , res, cnt = 1 ;
	cin >> t ;
	while ( t -- ) {
		cout <<"Case #"<<cnt++<<": ";
		cin >> s ;
		n = (int)s.size();
		cin >> k ;
		res = 0 ;
		for ( int i = 0 ; i < n ; i ++ ) {
			if ( s [ i ] == '-'){
				if ( i + k > n ) {
					res = -1;
					break ;
				}
				for ( int j = i ; j < i + k ; j ++ ) s [ j ] = ( s [ j ] == '+' ? '-' : '+' ) ;
				res ++ ;
			} 
		}
		if ( res == -1 ) cout << "IMPOSSIBLE" << endl ;
		else cout << res << endl ;
	}
}
