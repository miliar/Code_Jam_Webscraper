#include <bits/stdc++.h>

using namespace std;

#ifdef ONLINE_JUDGE
#define OJ 1
#else
#define OJ 0
#endif

#define dd				double
#define ll 				long long
#define pb 				push_back
#define mp 				make_pair
#define X				first
#define Y				second
#define forn( i, n ) 	for( ll i = 0; i < (ll) (n); i ++ )
#define endl 			'\n'

struct __s { __s() {
		srand( time( NULL ) );
		freopen( "A-large.in", "r", stdin ); freopen( "A.out", "w", stdout );
		if( OJ ) { ios_base::Init i; cin.sync_with_stdio( 0 ); cin.tie( 0 ); }
	}
} __S;

void solve2( ll t, vector< ll > &cnt ) {
	ll ans = 0;
	ans += cnt[0];
	ans += ( cnt[1] + 1 ) / 2;
	cout << "Case #" << t + 1 << ": " << ans << endl;
}

void solve3( ll t, vector< ll > &cnt ) {
	ll ans = 0;
	ans += cnt[0];
	ll mn = min( cnt[1], cnt[2] );
	ans += mn;
	cnt[1] -= mn;
	cnt[2] -= mn;
	ans += cnt[1] / 3;
	ans += cnt[2] / 3;
	cnt[1] %= 3;
	cnt[2] %= 3;
	if( cnt[1] || cnt[2] )
		ans ++;
	cout << "Case #" << t + 1 << ": " << ans << endl;
}

void solve4( ll t, vector< ll > &cnt ) {
	ll ans = 0;
	ans += cnt[0];
	ll mn = min( cnt[1], cnt[3] );
	ans += mn;
	cnt[1] -= mn;
	cnt[3] -= mn;
	ans += cnt[2] / 2;
	cnt[2] %= 2;
	ans += cnt[1] / 4;
	ans += cnt[3] / 4;
	cnt[1] %= 4;
	cnt[3] %= 4;
	if( cnt[2] >= 1 && cnt[1] >= 2 ) {
		ans ++;
		cnt[2] --;
		cnt[1] -= 2;
	}
	if( cnt[2] >= 1 && cnt[3] >= 2 ) {
		ans ++;
		cnt[2] --;
		cnt[3] -= 2;
	}
	if( cnt[2] || cnt[1] || cnt[3] )
		ans ++;
	cout << "Case #" << t + 1 << ": " << ans << endl;
}

int main( void ) {
	ll T;
	cin >> T;
	forn( t, T ) {
		ll n, p;
		cin >> n >> p;
		vector< ll > cnt( 5, 0 );
		forn( i, n ) {
			ll x;
			cin >> x;
			x %= p;
			cnt[x] ++;
		}
		if( p == 2 )
			solve2( t, cnt );
		else if( p == 3 )
			solve3( t, cnt );
		else if( p == 4 )
			solve4( t, cnt );
	}
	return 0;
}
