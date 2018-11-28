#include <bits/stdc++.h>
using namespace std;
int caso = 0;

void doit(){
	string s;
	int k;	
	cin >> s >> k;
	int sz = s.size();
	int ans = 0;
	for( int i=0; i <= sz-k; ++i ){
		if( s[ i ] == '-'){
			ans++;
			for( int j = i; j < i+k; ++j ){
				if( s[ j ] == '-') s[ j ] = '+';
				else s[ j ] = '-';
			}
		}
	}
	bool ok = 1;
	for( int i=0; i<sz; ++i ){
		if( s[ i ] == '-') ok = 0;
	}
	if( ok == 0 ) printf("Case #%d: IMPOSSIBLE\n", ++caso);
	else printf("Case #%d: %d\n", ++caso, ans );
}

int main(){
	int tc;
	cin >> tc;
	while( tc-- ) doit();	
	return 0;
}
