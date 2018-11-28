#include<iostream>
#include<set>
#include<algorithm>
#include<utility>
using namespace std;

#define X first
#define Y second
#define MP make_pair

int HD, Hd, Ad, Hk, Ak, B, D;

bool SEEN[ 101 ][ 301 ][ 101 ][ 101 ];

int main(){
	int T; cin >> T;
	for( int kase = 1; kase <= T; kase++ ){
		cin >> Hd >> Ad >> Hk >> Ak >> B >> D;
		for( int i = 0; i <= Hd; i++ ){
			for( int j = 0; j < 301; j++ ){
				for( int k = 0; k <= Hk; k++ ){
					for( int q = 0; q <= Ak; q++ ){
						SEEN[ i ][ j ][ k ][ q ] = false;
					}
				}
			}
		}
		HD = Hd;
		bool killed = false;
		int turn = 0;
		set< pair< pair< int, int > , pair< int, int > > > spp;
		spp.insert( MP( MP( Hd, Ad ), MP( Hk, Ak ) ) );
		SEEN[ Hd ][ Ad ][ Hk ][ Ak ] = true;
		while( !killed && spp.size() ){
			turn++;
			set< pair< pair< int, int > , pair< int, int > > > spp2;
			while( spp.size() ){
				pair< pair< int, int > , pair< int, int > > p = *spp.begin();
				spp.erase( spp.begin() );
				// cure
				if( p.X.X != HD ){
					pair< pair< int, int > , pair< int, int > > p2 = p;
					p2.X.X = HD - p2.Y.Y;
					if( p2.X.X > 0 && !SEEN[ p2.X.X ][ p2.X.Y ][ p2.Y.X ][ p2.Y.Y ] ){
						SEEN[ p2.X.X ][ p2.X.Y ][ p2.Y.X ][ p2.Y.Y ] = true;
						spp2.insert( p2 );
					}
				}
				// debuff
				if( D > 0 && p.Y.Y > 0 ){
					pair< pair< int, int > , pair< int, int > > p2 = p;
					p2.Y.Y = max( p2.Y.Y-D, 0 );
					p2.X.X -= p2.Y.Y;
					if( p2.X.X > 0 && !SEEN[ p2.X.X ][ p2.X.Y ][ p2.Y.X ][ p2.Y.Y ] ){
						SEEN[ p2.X.X ][ p2.X.Y ][ p2.Y.X ][ p2.Y.Y ] = true;
						spp2.insert( p2 );
					}
				}
				// buff
				if( B > 0 ){
					pair< pair< int, int > , pair< int, int > > p2 = p;
					p2.X.Y += B;
					p2.X.X -= p2.Y.Y;
					if( p2.X.X > 0 && !SEEN[ p2.X.X ][ p2.X.Y ][ p2.Y.X ][ p2.Y.Y ] ){
						SEEN[ p2.X.X ][ p2.X.Y ][ p2.Y.X ][ p2.Y.Y ] = true;
						spp2.insert( p2 );
					}
				}
				// Attack
				p.Y.X -= p.X.Y; p.X.X -= p.Y.Y;
				if( p.Y.X <= 0 ){ killed = true; break; }
				if( p.X.X > 0 ){
					SEEN[ p.X.X ][ p.X.Y ][ p.Y.X ][ p.Y.Y ] = true;
					spp2.insert( p );
				}
			}
			swap( spp2, spp );
		}
		if( !killed ) cout << "Case #" << kase << ": IMPOSSIBLE" << endl;
		else cout << "Case #" << kase <<": " << turn << endl;
	}
}
