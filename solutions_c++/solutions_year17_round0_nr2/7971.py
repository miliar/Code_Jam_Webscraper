#include <cstdio>
#include <cstring>
#include <iostream>

#define SIZE(a) ((int)a.size())

using namespace std;

typedef long long int Lint;

int T;

int main(){
	
	string s;
	
	scanf("%d",&T);
	
	for( int Case=1 ; Case <= T ; Case++ ){
		
		cin >> s;
		
		for( int k=0 ; k<20 ; k++ )
			for( int i=0 ; i <SIZE(s)-1 ; i++ )
				if( s[i] > s[i+1] ){
					
					s[i]--;
					for( int j=i+1 ; j<SIZE(s) ; j++ )
						s[j] = '9';
					
					break;
				}
		
		if( s[0] == '0' )
			s.erase(0,1);
			
		cout << "Case #" << Case << ": " << s << endl;		
	}
	
	return 0;
}
