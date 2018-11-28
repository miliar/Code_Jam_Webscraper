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
		freopen( "A-large.in", "r", stdin ); freopen( "A-large.out", "w", stdout );
		if( OJ ) { ios_base::Init i; cin.sync_with_stdio( 0 ); cin.tie( 0 ); }
	}
} __S;


int main( void ) {
	ll T;
	cin >> T;
	forn( t, T ) {
		ll n, m;
		cin >> n >> m;
		vector< string > s( n );
		forn( i, n ) {
			cin >> s[i];
			forn( j, m ) {
				if( s[i][j] != '?' )
					continue;
				if( j - 1 >= 0 && s[i][j - 1] != '?' )
					s[i][j] = s[i][j - 1];
			}
			forn( jj, m ) {
				ll j = m - 1 - jj;
				if( s[i][j] != '?' )
					continue;
				if( j + 1 < m && s[i][j + 1] != '?' )
					s[i][j] = s[i][j + 1];
			}
		}
		forn( i, n ) {
			if( s[i][0] != '?' )
				continue;
			if( i - 1 >= 0 && s[i - 1][0] != '?' )
				s[i] = s[i - 1];
		}
		forn( ii, n ) {
			ll i = n - 1 - ii;
			if( s[i][0] != '?' )
				continue;
			if( i + 1 < n && s[i + 1][0] != '?' )
				s[i] = s[i + 1];
		}
		cout << "Case #" << t + 1 << ": " << endl;
		forn( i, n ) {
			cout << s[i] << endl;
		}
	}
	return 0;
}
