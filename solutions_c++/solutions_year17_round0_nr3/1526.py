#include <bits/stdc++.h>
using namespace std;

#define ll long long int
#define vi vector<ll>
#define vvi vector<vi>
#define pb push_back
#define forn(i,n) for( i = 0; i < n; i++ )
#define s(n) scanf("%lld",&n);
#define MODN 1000000007

vector< map<ll,ll> > mp(101);
map<ll, ll> :: iterator it;
vi val, cnt;
int main()
{
	freopen("in3.txt","r",stdin);
	freopen("out3.txt","w",stdout);

	ll i, j, ii, t, n, k;
	s(t);
	for( ii = 1 ; ii <= t ; ii++ )
	{
		s(n); s(k);
		mp[0].clear();
		mp[0][n] = 1;
		
		ll ans, pow2 = 1;
		for( i = 1; i <= n ; i++){
			mp[i].clear();
			val.clear();
			cnt.clear();
			for( it = mp[i-1].begin(); it != mp[i-1].end(); it++ ){
				val.pb(it -> first); cnt.pb(it -> second);
				mp[i][ val.back() / 2 ] += cnt.back();
				mp[i][ ( val.back() - 1 ) / 2 ] += cnt.back();
			}
			if( k > pow2 )
				k -= pow2;
			else{
				if( mp[i-1].size() == 1 ) ans = val[0];
				else ans = ( k > cnt[1] ) ? val[0] : val[1];
				break;
			}
			pow2 *= 2;
		}
		cout << "Case #" << ii << ": " << ans / 2 << " " << ( ans - 1 ) / 2 << endl;
	}
}
