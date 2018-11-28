#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	
	int t , k , u = 0  ;
	int vi[1101] ;
	
	
	cin >> t; 
	
	while ( t-- ){
		
		u++;
		string s ;
		int ans = 0 ;
		bool c = 0 ;
		
		memset ( vi , 0 , sizeof(vi) ) ;
		
		cin >> s >> k ;
		//cout << k << " " << s << endl ;
		for  ( int i = 0 ; i < s.length( ) ; i++ ) {
			
			if ( vi[i] == 1 ){
				c = !c ;
			}
				
			if ( c%2 != 0 ) {
				
				if ( s[i] == '+' ){
					s[i] = '-' ;
				}else{
					s[i] = '+' ;
				}
				
			}	
				
				
			if ( s[i] == '-' ){
				
				if ( i + k > s.length( ) ) {
					ans = -1 ;
					break;
					
				}
				
				c = !c ;
				vi[i+k] = 1 ;
				ans++;
			}
				
		}
		
		if ( ans == -1 ){
			cout << "Case #"<< u <<": "<< "IMPOSSIBLE" << endl;
		}
		else {cout << "Case #"<< u <<": "<< ans << endl ;}
		
	}
	
	
	
	return 0;
}
