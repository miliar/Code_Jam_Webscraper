#include<bits/stdc++.h>
using namespace std ;

int getTidyPartition(string str){
	for( int i = 1 ; i < str.size() ; i++ )
		if( str[i] < str[i-1] ) return i-1 ;
	
	return -1 ;
}

int main() {

	freopen("in.txt","r",stdin) ;
	freopen("out.txt","w",stdout) ;
	int t , n ;
	string str ;
	cin >> t ;
	for( int k = 1 ; k <= t ; k++ ) {
		cin >> str ;
		int counter = 0 ;
		cout << "Case #" << k << ": " ;
		int pos = getTidyPartition(str) ;
		if( pos == -1 )
			 cout << str << endl ;
		else {
			int j = pos ;
			while( (j >= 0) && (str[j] == str[pos]) ){
				
				j-- ;
			}
			
			if( (j < 0) && ( str[0] == '1' ) ) {
				for( int i = 0 ; i < str.size()-1 ; i++ ) cout << 9 ;
				cout << endl ;
			}else {
				j++ ;
				str[j]-- ;
				j++ ;
				for( ; j < str.size() ; j++ ) str[j] = '9' ;
				cout << str << endl ;
			}	
		}

	}
	return 0 ;

}
