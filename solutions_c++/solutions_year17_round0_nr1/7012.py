#include <bits/stdc++.h>

using namespace std;


ifstream in("1.in");
ofstream out("1.out");

int main(){
	
	int test_case;
	in >> test_case;
	int cou=1;
	
	
	while( test_case-- > 0 ){
			
		string s;
		int a,n;
		in >> s >> a;
		
		n = s.size();
		
		bool f=1;
		
		int ans=0;
		
		for( int i=0;i<n;i++){
			if( s[i] == '-' and n-i >= a ){
				ans++;
				for( int j=i+1;j<i+a;j++){
					if( s[j] == '-' ) 	s[j] = '+';
					else 				s[j] = '-';
				}
			}else if( s[i] == '-' ){
				f=0;	
			}
		}
		
		out << "Case #" << cou++ << ": ";
		if( f == 0 ) 	out << "IMPOSSIBLE\n";
		else 			out << ans << endl;
		
	}
	return 0;	
}
