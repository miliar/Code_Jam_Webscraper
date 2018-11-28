#include <bits/stdc++.h>

using namespace std;

#ifdef ONLINE_JUDGE
#define OJ 1
#else
#define OJ 0
#endif

#define dd				double
#define ll 				int
#define pb 				push_back
#define mp 				make_pair
#define X				first
#define Y				second
#define forn( i, n ) 	for( ll i = 0; i < (ll) (n); i ++ )
#define endl 			'\n'

struct __s { __s() {
		srand( time( NULL ) );
		freopen( "B-large.in", "r", stdin ); freopen( "B.out", "w", stdout );
		if( OJ ) { ios_base::Init i; cin.sync_with_stdio( 0 ); cin.tie( 0 ); }
	}
} __S;

ll check( ll n, ll c, ll m, ll k, vector< ll > v ) {
	ll res = 0;
	ll sum = 0;
	for( ll i = n-1; i >= 0; i -- ) {
		ll cnt = k;
		if( cnt < v[i] ) {
			res += v[i] - cnt;
			sum += v[i] - cnt;
		} else {
			cnt -= v[i];
			sum = max( 0, sum - cnt );
		}
	}
	if( sum )
		return -1;
	return res;
}

int main( void ) {
	cout << fixed << setprecision( 10 );
	ll T;
	cin >> T;
	forn( t, T ) {
		ll n, c, m;
		cin >> n >> c >> m;
		vector< ll > v( n );
		vector< ll > cnt( c, 0 );
		ll ans = 0;
		forn( i, m ) {
			ll p, b;
			cin >> p >> b;
			p --, b --;
			cnt[b] ++;
			ans = max( ans, cnt[b] );
			v[p] ++;
		}
		ll l = ans;
		ll r = m;
		while( l != r ) {
			ll mid = ( l + r ) >> 1;
			if( check( n, c, m, mid, v ) != -1 )
				r = mid;
			else
				l = mid + 1;
		}
		ans = l;
		ll res = check( n, c, m, ans, v );
		cout << "Case #" << t + 1 << ": " << ans << " " << res << endl;
	}
	return 0;
}
