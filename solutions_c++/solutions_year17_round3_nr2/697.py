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
		freopen( "B-large.in", "r", stdin ); freopen( "B_out.out", "w", stdout );
		if( OJ ) { ios_base::Init i; cin.sync_with_stdio( 0 ); cin.tie( 0 ); }
	}
} __S;

int main( void ) {
	ll T;
	cin >> T;
	forn( t, T ) {
		ll n, m;
		cin >> n >> m;
		vector< pair< ll, ll > > a( n ), b( m );
		forn( i, n ) {
			cin >> a[i].X >> a[i].Y;
		}
		forn( i, m ) {
			cin >> b[i].X >> b[i].Y;
		}
		if( n > m ) {
			swap( n, m );
			swap( a, b );
		}
		if( m == 1 ) {
			cout << "Case #" << t + 1 << ": " << m * 2 << endl;
			continue;
		}
		vector< bool > use( 24*60, false );
		forn( i, n ) {
			for( ll j = a[i].X; j < a[i].Y; j ++ ) {
				use[j] = true;
			}
		}
		vector< ll > s( 24*60, 0 );
		forn( i, 24*60 ) {
			s[i] = use[i];
			if( i )
				s[i] += s[i-1];
		}
		ll sum = 0;
		forn( i, m ) {
			sum += ( b[i].Y - b[i].X );
		}
		sort( b.begin(), b.end() );
		while( m != 1 ) {
			ll res = 1e18;
			ll idx = -1;
			forn( i, b.size()-1 ) {
				ll l = b[i].Y;
				ll r = b[i+1].X;
				ll dist = r - l;
				ll cnt = s[r] - s[l] + use[l];
				if( cnt > 0 )
					continue;
				if( res > dist ) {
					res = dist;
					idx = i;
				}
			}
			{
				ll l = b.back().Y;
				ll r = b.front().X;
				ll dist = r - l + 24*60;
				ll cnt = 0;
				if( l < 24*60 )
					cnt += s[24*60-1] - s[l] + use[l];
				cnt += s[r];
				if( cnt == 0 && res > dist ) {
					res = dist;
					idx = b.size()-1;
				}
			}
			if( idx == -1 )
				break;
			if( sum + res > 720 )
				break;
			sum += res;
			m --;
			if( idx != b.size()-1 ) {
				vector< pair< ll, ll > > v;
				for( ll i = 0; i < idx; i ++ ) {
					v.pb( b[i] );
				}
				v.pb( mp( b[idx].X, b[idx+1].Y ) );
				for( ll i = idx + 2; i < b.size(); i ++ ) {
					v.pb( b[i] );
				}
				b = v;
			} else {
				vector< pair< ll, ll > > v;
				for( ll i = 1; i < idx; i ++ ) {
					v.pb( b[i] );
				}
				v.pb( mp( b.back().X, b.front().Y ) );
				b = v;
			}
		}
		sum = 0;
		forn( i, b.size() ) {
			ll x = b[i].X;
			while( x >= 0 && !use[x] ) {
				use[x] = true;
				sum ++;
				x --;
			}
			x = b[i].X + 1;
			while( x < 24*60 && !use[x] ) {
				use[x] = true;
				sum ++;
				x ++;
			}
		}
		m += ( sum < 720 );
		cout << "Case #" << t + 1 << ": " << m * 2 << endl;
	}
	return 0;
}
