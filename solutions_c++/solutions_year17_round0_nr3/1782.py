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
		freopen( "C-large.in", "r", stdin ); freopen( "C-large.out", "w", stdout );
		if( OJ ) { ios_base::Init i; cin.sync_with_stdio( 0 ); cin.tie( 0 ); }
	} ~__s() {
		if( !OJ ) TIMESTAMP;
		ll n; cin >> n;
	}
} __S;

pair< ll, ll > get( ll len ) {
	ll l = 1;
	ll r = len;
	ll mid = ( l + r ) / 2;
	ll ls = mid - l;
	ll rs = r - mid;
	return mp( ls, rs );
}

void add( ll len, ll cnt, priority_queue< ll > &q, map< ll, ll > &m ) {
	if( len == 0 )
		return;
	if( m.find( len ) == m.end() )
		q.push( len );
	m[len] += cnt;
}

int main( void ) {
	ll T;
	cin >> T;
	forn( t, T ) {
		ll n, k;
		cin >> n >> k;
		priority_queue< ll > q;
		map< ll, ll > m;
		add( n, 1, q, m );
		while( k ) {
			ll len = q.top();
			q.pop();
			ll cnt = m[len];
			pair< ll, ll > p = get( len );
			if( cnt >= k ) {
				cout << "Case #" << t + 1 << ": " << p.Y << " " << p.X << endl;
				break;
			}
			k -= cnt;
			add( p.X, cnt, q, m );
			add( p.Y, cnt, q, m );
		}
	}
	return 0;
}
