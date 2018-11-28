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
		freopen( "B-small-attempt1.in", "r", stdin ); freopen( "B-small-attempt1.out", "w", stdout );
		if( OJ ) { ios_base::Init i; cin.sync_with_stdio( 0 ); cin.tie( 0 ); }
	}
} __S;

const ll MX = 1200000;

ll l[MX];
ll r[MX];

ll n, p;

bool in( ll l, ll r, ll x ) {
	return ( l <= x && x <= r );
}

vector< ll > get( ll sum, vector< ll > &a ) {
	vector< ll > res;
	bool ok = false;
	for( ll i = 1; a[0] * i < MX; i ++ ) {
		ll j = a[0] * i;
		if( in( l[j], r[j], sum ) ) {
			ok = true;
			res.pb( i );
		} else if( ok )
			break;
	}
	return res;
}

ll rec( ll ans, ll I, ll J, vector< vector< ll > > &u ) {
	ll res = ans;
	if( res == p ) {
		return res;
	}
	forn( i, u.size() ) {
		if( I & ( 1 << i ) )
			continue;
		forn( jj, u[i].size() ) {
			ll j = u[i][jj];
			if( J & ( 1 << j ) )
				continue;
			res = max( res, rec( ans + 1, I | ( 1 << i ), J | ( 1 << j ), u ) );
			if( res == p )
				return res;
		}
	}
	return res;
}

int main( void ) {
	forn( i, MX ) {
		l[i] = ( i * 9 + 9 ) / 10;
		r[i] = ( i * 11 ) / 10;
	}
	ll T;
	cin >> T;
	forn( t, T ) {
		cin >> n >> p;
		vector< ll > a( n );
		forn( i, n ) {
			cin >> a[i];
		}
		vector< vector< ll > > v( n, vector< ll >( p ) );
		forn( i, n ) {
			forn( j, p ) {
				cin >> v[i][j];
			}
		}
		vector< vector< ll > > u( p );
		forn( i, p ) {
			vector< ll > w = get( v[0][i], a );
			if( w.size() == 0 )
				continue;
			if( n == 1 ) {
				u[i].pb( i );
				continue;
			}
			forn( j, p ) {
				forn( ii, w.size() ) {
					ll cnt = w[ii];
					ll sum = cnt * a[1];
					if( sum >= MX )
						break;
					if( in( l[sum], r[sum], v[1][j] ) ) {
						u[i].pb( j );
						break;
					}
				}
			}
		}
		ll ans = rec( 0, 0, 0, u );
		cout << "Case #" << t + 1 << ": " << ans << endl;
	}
	return 0;
}
