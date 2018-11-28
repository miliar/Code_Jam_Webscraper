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
		freopen( "B-large.in", "r", stdin ); freopen( "B-large.out", "w", stdout );
		if( OJ ) { ios_base::Init i; cin.sync_with_stdio( 0 ); cin.tie( 0 ); }
	}
} __S;


int main( void ) {
	ll T;
	cin >> T;
	forn( t, T ) {
		cout << "Case #" << t + 1 << ": ";
		ll n;
		cin >> n;
		ll r, o, y, g, b, v;
		cin >> r >> o >> y >> g >> b >> v;
		if( o > b || g > r || v > y ) {
			cout << "IMPOSSIBLE" << endl;
			continue;
		}
		string ob, gr, vy;
		bool OB = false;
		bool GR = false;
		bool VY = false;
		if( n == o + b && o == b ) {
			forn( i, n / 2 ) {
				cout << "OB";
			}
			cout << endl;
			continue;
		} else if( o != 0 && b == o ) {
			cout << "IMPOSSIBLE" << endl;
			continue;
		} else if( o != 0 ) {
			OB = true;
			ob += 'B';
			forn( i, o ) {
				ob += 'O';
				ob += 'B';
				b --;
			}
		}
		if( n == g + r && g == r ) {
			forn( i, n / 2 ) {
				cout << "GR";
			}
			cout << endl;
			continue;
		} else if( g != 0 && r == g ) {
			cout << "IMPOSSIBLE" << endl;
			continue;
		} else if( g != 0 ) {
			GR = true;
			gr += 'R';
			forn( i, g ) {
				gr += 'G';
				gr += 'R';
				r --;
			}
		}
		if( n == v + y && v == y ) {
			forn( i, n / 2 ) {
				cout << "VY";
			}
			cout << endl;
			continue;
		} else if( v != 0 && v == y ) {
			cout << "IMPOSSIBLE" << endl;
			continue;
		} else if( v != 0 ) {
			VY = true;
			vy += 'Y';
			forn( i, v ) {
				vy += 'V';
				vy += 'Y';
				y --;
			}
		}
		ll sum = r + y + b;
		ll mx = max( r, max( y, b ) );
		if( mx > sum - mx ) {
			cout << "IMPOSSIBLE" << endl;
			continue;
		}
		vector< string > s;
		char old = ' ';
		forn( i, sum ) {
			if( r >= y && r >= b && old != 'R' ) {
				if( GR ) {
					s.pb( gr );
					GR = false;
				} else
					s.pb( "R" );
				r --;
			} else if( b >= y && b >= r && old != 'B' ) {
				if( OB ) {
					s.pb( ob );
					OB = false;
				} else
					s.pb( "B" );
				b --;
			} else if( y >= r && y >= b && old != 'Y' ) {
				if( VY ) {
					s.pb( vy );
					VY = false;
				} else
					s.pb( "Y" );
				y --;
			} else if( old == 'R' && y != 0 && y >= b ) {
				if( VY ) {
					s.pb( vy );
					VY = false;
				} else
					s.pb( "Y" );
				y --;
			} else if( old == 'R' && b != 0 && b >= y ) {
				if( OB ) {
					s.pb( ob );
					OB = false;
				} else
					s.pb( "B" );
				b --;
			} else if( old == 'Y' && r != 0 && r >= b ) {
				if( GR ) {
					s.pb( gr );
					GR = false;
				} else
					s.pb( "R" );
				r --;
			} else if( old == 'Y' && b != 0 && b >= r ) {
				if( OB ) {
					s.pb( ob );
					OB = false;
				} else
					s.pb( "B" );
				b --;
			} else if( old == 'B' && r != 0 && r >= y ) {
				if( GR ) {
					s.pb( gr );
					GR = false;
				} else
					s.pb( "R" );
				r --;
			} else if( old == 'B' && y != 0 && y >= r ) {
				if( VY ) {
					s.pb( vy );
					VY = false;
				} else
					s.pb( "Y" );
				y --;
			}
			old = s[i][s[i].size()-1];
		}
		if( s.size() > 1 && s[0][0] == s[s.size()-1][s[s.size()-1].size()-1] )
			swap( s[s.size()-2], s[s.size()-1] );
		if( s.size() > 2 && s[s.size()-3][s[s.size()-3].size()-1] == s[s.size()-2][0] )
			cout << "ERROR" << endl;
		forn( i, s.size() ) {
			cout << s[i];
		}
		cout << endl;
	}
	return 0;
}
