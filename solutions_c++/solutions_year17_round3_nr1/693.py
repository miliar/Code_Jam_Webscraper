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
		freopen( "A-large.in", "r", stdin ); freopen( "A_out.out", "w", stdout );
		if( OJ ) { ios_base::Init i; cin.sync_with_stdio( 0 ); cin.tie( 0 ); }
	}
} __S;

dd Pi = acos( -1.0 );

ll sqr( ll x ) {
	return x * x;
}

ll dp[1111][1111];

void del() {
	forn( i, 1111 ) {
		forn( j, 1111 ) {
			dp[i][j] = 0;
		}
	}
}

int main( void ) {
	ll T;
	cin >> T;
	forn( t, T ) {
		del();
		ll n, k;
		cin >> n >> k;
		vector< pair< ll, ll > > a( n+1 );
		for( ll i = 1; i <= n; i ++ ) {
			cin >> a[i].X >> a[i].Y;
		}
		sort( a.begin(), a.end() );
		ll ans = 0;
		for( ll i = 1; i <= n; i ++ ) {
			forn( l, i ) {
				for( int j = 1; j <= k; j ++ ) {
					ll res = dp[l][j-1];
					res += 2 * a[i].X * a[i].Y;
					res -= sqr( a[l].X );
					res += sqr( a[i].X );
					dp[i][j] = max( dp[i][j], res );
					ans = max( ans, res );
				}
			}
		}
		cout << fixed << setprecision( 10 );
		cout << "Case #" << t + 1 << ": " << Pi * ans << endl;
	}
	return 0;
}
