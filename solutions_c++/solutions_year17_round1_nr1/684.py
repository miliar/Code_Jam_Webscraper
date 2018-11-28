#include <bits/stdc++.h>
using namespace std;

#define ll long long int
#define vi vector<ll>
#define vvi vector<vi>
#define pb push_back
#define forn(i,n) for( i = 0; i < n; i++ )
#define s(n) scanf("%lld",&n);
#define MODN 1000000007
string str[30];
int main()
{
	freopen("in1.txt","r",stdin);
	freopen("out1.txt","w",stdout);
	ll i, j, k, ii, t;
	s(t);
	for( ii = 1 ; ii <= t ; ii++ )
	{
		ll n, m;
		s(n); s(m);
		for( i = 0; i < n; i++ ){
			cin >> str[i];
		}
		for( i = 0; i < n; i++ ){
			for( j = 0; j < m; j++ ){
				if( str[i][j] != '?' ){
					for( k = j + 1; k < m; k++ ){
						if( str[i][k] != '?' ) break;
						else str[i][k] = str[i][j];
					}
					for( k = j - 1; k >= 0; k-- ){
						if( str[i][k] != '?' ) break;
						else str[i][k] = str[i][j];
					}	
				}
			}
		}	
		for( i = 0; i < n-1; i++ ){
			for( j = 0; j < m; j++ ){
				if( str[i][j] != '?' && str[i+1][j] == '?' )
					str[i+1][j] = str[i][j];
			}
		}
		for( i = n-1; i > 0; i-- ){
			for( j = 0; j < m; j++ ){
				if( str[i][j] != '?' && str[i-1][j] == '?' )
					str[i-1][j] = str[i][j];
			}
		}
		cout << "Case #" << ii << ":" << endl;
		for( i = 0; i < n; i++ )
				cout << str[i] << endl;
	}
}
