#include <bits/stdc++.h>
using namespace std;
#define ll long long int
#define vi vector<ll>
#define vvi vector<vi>
#define pb push_back
#define forn(i,n) for( i = 0; i < n; i++ )
#define s(n) scanf("%lld",&n);
#define MODN 1000000007

int main() {
	freopen("in2.txt","r",stdin);
	freopen("out2.txt","w",stdout);
	string str;
    ll i, j, n, ii, t;
	s(t);
	for( ii = 1 ; ii <= t ; ii++ )
	{
		cin >> str;
		n = str.length();
		ll ptr = 0;
		for( i = 0; i < n-1; i++ ){
			if( str[i] < str[i+1] ) ptr = i + 1;
			else if( str[i] > str[i+1] ){
				str[ptr]--;
				for( j = ptr+1; j < n; j++ ) str[j] = '9';
				break;
			}
		}
		ll ans = stoll(str);
		cout << "Case #" << ii << ": " << ans << endl;
	}
    return 0;
}
