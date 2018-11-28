#include<bits/stdc++.h>
using namespace std;
string s;
int k, n, T[ 1002 ];

int main(){
	int cases;
	cin>>cases;
	for ( int tt = 0 ; tt < cases ; tt++ ){	
		cin>>s;
		n = (int)s.size();
		cin>>k;
		bool ok = 1;
		int res = 0 , ans = 0;
		memset( T , 0 , sizeof( T ) );
		for ( int i = 0 ; i < n ; i++ ){
			if ( ans % 2 == 0 ){
				if ( s[ i ] == '-'){
					if ( i + k - 1 < n )T[ i + k - 1 ]++;
					else{
						ok = 0;
						break;
					}
					res++;
					ans++;
				}
				ans -= T[ i ];
			}else{
				if ( s[ i ] == '+' ){
					if ( i + k - 1 < n ) T[ i + k - 1 ]++;
					else{
						ok = 0;
						break;
					}
					res++;
					ans++;
				}
				ans -= T[ i ];
			}
		}
		if ( ok ){
			printf("Case #%d: %d\n",tt+1,res);	
		}else{
			printf("Case #%d: IMPOSSIBLE\n",tt+1);
		}
	}
}
