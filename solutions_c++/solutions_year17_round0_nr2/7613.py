#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	
	int t , n , minn , len ;
	int vi[1101] ;
	string s ;
	int u = 1 ;
	
	cin >> t; 
	
	while ( t-- ){
		
		
		cin >> s ;
		len = s.length()-1 ;
		minn = s[len]-'0' ;
		vi[len] = minn ;
		
		for ( int i = len-1 ; i >= 0 ; i-- ) {
			
			n = s[i]-'0' ;
			
			if ( n < minn ) {
				
				minn = n ;
				
				
			}
			vi[i] = minn ;
			
		}
		
		string ans = "" ;
		int j ;
		
		for ( int i = 0 ; i < s.length() ; i++ ){
			
			if ( s[i]-'0' > vi[i] ){
				
				string temp ;
				
				temp += s[i] ;
					
				for (  j = i+1 ; j < len+1 ; j++ ){
					if ( (s[j]-'0') < (s[i]-'0') ){
						j = i+1 ;
						
						if ( s[i] == '1' )
							ans = "" ;
						else	ans += s[i] - 1 ;
						
						break;
					}
					
					else if ( (s[j]-'0') > (s[i]-'0') ){
						
						ans += temp ;
						ans += s[j]-1 ;
						j++;
						break ;
					}
					
					else{
						temp += s[i] ;
					}
				}	
				
				for ( ; j < len+1 ; j++ ){
						ans += '9' ;
				}
				break ;
				
			}
			
			ans += s[i] ;
		}
		
			cout <<"Case #"<<u<<": "<< ans << endl ;
			u++;
		
	}
	/*99999999999999999
	9999999999999999 
	111111111111111110
	99999999999999999*/
	
	
	return 0;
}
