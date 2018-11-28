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

#define TIMESTAMP fprintf(stderr, "Execution time: %.3lf s.\n", (double)clock()/CLOCKS_PER_SEC)

struct __s { __s() {
		srand( time( NULL ) );
		freopen( "B-large.in", "r", stdin ); freopen( "B-large.out", "w", stdout );
		if( OJ ) { ios_base::Init i; cin.sync_with_stdio( 0 ); cin.tie( 0 ); }
	} ~__s() {
		if( !OJ ) TIMESTAMP;
		ll n; cin >> n;
	}
} __S;


int main( void ) {
	ll T;
	cin >> T;
	forn( t, T ) {
		string s;
		cin >> s;
		string ans;
		for( ll i = (ll) s.size() - 2; i >= 0; i -- ) {
			if( s[i] <= s[i + 1] )
				continue;
			s[i] --;
			for( ll j = i + 1; j < s.size(); j ++ )
				s[j] = '9';
		}
		forn( i, s.size() ) {
			if( s[i] == '0' && ans.size() == 0 )
				continue;
			ans += s[i];
		}
		cout << "Case #" << t + 1 << ": " << ans << endl;
	}
	return 0;
}
