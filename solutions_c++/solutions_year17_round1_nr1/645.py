#include <bits/stdc++.h>
using namespace std;
#define ll long long
ll i, j, k, ii, t;
string s[30];
int main()
{
	cin>>t;
	for(ll _t = 1 ; _t <= t ; _t++ )
	{
		ll n, m;
		cin>>n>>m;
		for( i = 0; i < n; i++ ) {
			cin>>s[i];
		}
		for( i = 0; i < n-1; i++ ) {
			for( j = 0; j < m; j++ ) {
				if( s[i][j] != '?' && s[i+1][j] == '?' )
					s[i+1][j] = s[i][j];
			}
		}
		for( i = n-1; i > 0; i-- ) {
			for( j = 0; j < m; j++ ) {
				if( s[i][j] != '?' && s[i-1][j] == '?' )
					s[i-1][j] = s[i][j];
			}
		}
		for( i = 0; i < n; i++ ) {
			for( j = 0; j < m; j++ ) {
				if( s[i][j] == '?' ) continue;
                for( k = j + 1; k < m; k++ ) {
                    if( s[i][k] != '?' ) break;
                    else s[i][k] = s[i][j];
                }
                for( k = j - 1; k >= 0; k-- ) {
                    if( s[i][k] != '?' ) break;
                    else s[i][k] = s[i][j];
				}
			}
		}

		printf("Case #%lld:\n", _t);
		for( i = 0; i < n; i++ )
				cout << s[i] << endl;
	}
}
