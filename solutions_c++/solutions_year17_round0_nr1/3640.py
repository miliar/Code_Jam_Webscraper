#include<bits/stdc++.h>
using namespace std ;

bool isValid(string str){
	int i = 0 , counter = 0 ; 
	while( str[i] ){
		if( str[i] == '+' ) counter++ ;
		i++ ;
	}
	return counter == str.size() ;
}

int main() {

	freopen("in.txt","r",stdin) ;
	freopen("out.txt","w",stdout) ;
	int t , n ;
	string str ;
	cin >> t ;
	for( int k = 1 ; k <= t ; k++ ) {
		cin >> str >> n ;
		int counter = 0 ;
		
		int i = 0,j, len = str.size() ;
		while( str[i] ){
			
			if( i+n-1 >= len ) break ;
			
			if( str[i] == '-' ){
				j = 0 ;
				while( j < n ){
					if( str[i+j] == '-' ) str[i+j] = '+' ;
					else str[i+j] = '-' ;
					j++ ;
				}
				counter++ ;
			}
			
			//cout << str << endl ;
			i++ ;
			
		}
		
		if( isValid(str) )
				cout << "Case #" << k << ": " << counter << endl ;
		else 	cout << "Case #" << k << ": " << "IMPOSSIBLE" << endl ;

	}
	return 0 ;

}
