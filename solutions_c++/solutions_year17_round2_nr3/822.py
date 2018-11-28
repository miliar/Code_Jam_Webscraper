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
		freopen( "C-small-attempt0.in", "r", stdin ); freopen( "C-small-attempt0.out", "w", stdout );
		if( OJ ) { ios_base::Init i; cin.sync_with_stdio( 0 ); cin.tie( 0 ); }
	}
} __S;


int main( void ) {
	cout << fixed << setprecision( 10 );
	ll T;
	cin >> T;
	forn( t, T ) {
		ll n, q;
		cin >> n >> q;
		vector< ll > e( n );
		vector< ll > s( n );
		forn( i, n ) {
			cin >> e[i] >> s[i];
		}
		vector< vector< ll > > d( n, vector< ll >( n ) );
		vector< dd > D( n );
		forn( i, n ) {
			forn( j, n ) {
				cin >> d[i][j];
				if( i < j && d[i][j] != -1 )
					D[j] = d[i][j];
			}
		}
		ll st, fi;
		cin >> st >> fi;
		vector< vector< dd > > dp( n, vector< dd >( n, 1e18 ) );
		dp[0][0] = 0.0;
		vector< ll > v;
		v.pb( 0 );
		for( ll i = 1; i < n; i ++ ) {
			vector< ll > w;
			dd mn = 1e18;
			forn( jj, v.size() ) {
				ll j = v[jj];
				if( e[j] < D[i] )
					continue;
				e[j] -= D[i];
				w.pb( j );
				dp[i][j] = min( dp[i][j], dp[i-1][j] + ( D[i] * 1.0 / s[j] ) );
				mn = min( mn, dp[i][j] );
			}
			v = w;
			v.pb( i );
			dp[i][i] = mn;
		}

		cout << "Case #" << t + 1 << ": " << dp[n-1][n-1] << endl;
	}
	return 0;
}
