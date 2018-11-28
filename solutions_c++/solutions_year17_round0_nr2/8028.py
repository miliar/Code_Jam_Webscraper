#include<bits/stdc++.h>
using namespace std;
int main(){
	ios::sync_with_stdio(0);
	cin.tie(NULL);
	string s;
	int t , tt = 0;
	cin >> t ;
	while ( t-- ) {
		cin >> s ;
		int pos = 0 , val = 0 ;
		for ( int i = 0 ; i < (int) s.size() ; i ++ ) {
			if ( s [ i ] - '0' > val ){
				pos = i ;
				val = s [ i ] - '0' ;
			}else if ( s [ i ] - '0' < val ){
				s [ pos ] -- ;
				for ( int j = pos + 1 ; j < s.size() ; j ++ ) s [ j ] = '9';
				break ;
			}
		}
		if ( s [ 0 ] == '0' ) s = s.substr ( 1 , s.size() ) ;
		cout << "Case #" << ++ tt << ": " << s << endl ;
	}
}
