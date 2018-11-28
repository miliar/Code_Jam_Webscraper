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

bool check( dd t, dd d, vector< pair< dd, dd > > &v ) {
	vector< dd > x( v.size() );
	for( ll i = v.size()-1; i >= 0; i -- ) {
		x[i] = v[i].X + t * v[i].Y;
		if( i+1 < v.size() )
			x[i] = min( x[i], x[i+1] );
	}
	return x[0] >= d;
}

int main( void ) {
	cout << fixed << setprecision( 10 );
	ll T;
	cin >> T;
	forn( t, T ) {
		ll d, n;
		cin >> d >> n;
		vector< pair< dd, dd > > v( n );
		forn( i, n ) {
			cin >> v[i].X >> v[i].Y;
		}
		sort( v.begin(), v.end() );
		dd l = 0.0;
		dd r = 1e18;
		forn( _, 555 ) {
			dd mid = ( l + r ) / 2.0;
			if( check( mid, d, v ) )
				r = mid;
			else
				l = mid;
		}
		cout << "Case #" << t + 1 << ": " << d / l << endl;
	}
	return 0;
}
