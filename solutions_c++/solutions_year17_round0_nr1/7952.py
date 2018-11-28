#include <cstdio>
#include <cstring>
#include <iostream>

#define SIZE(a) ((int)a.size())

using namespace std;

typedef long long int Lint;

int T,K;

int main(){
	
	string s;
	
	scanf("%d",&T);
	
	for( int Case=1 ; Case <= T ; Case++ ){
		
		int res=0;
		
		cin >> s >> K;
		
		for( int i=0 ; i<=SIZE(s)-K ; i++ )
			if( s[i] == '-' ){
				res++;
				for( int j=i ; j<i+K ; j++ )
					if( s[j] == '+' )
						s[j] = '-';
					else
						s[j] = '+';
			}
		
		for( int i=SIZE(s)-K ; i<SIZE(s) ; i++ )
			if( s[i] == '-' ){
				res = -1;
				break;
			}
		
		if( res != -1 )	
			cout << "Case #" << Case << ": " << res << endl;
		else
			cout << "Case #" << Case << ": IMPOSSIBLE" << endl;
	}
	
	return 0;
}
