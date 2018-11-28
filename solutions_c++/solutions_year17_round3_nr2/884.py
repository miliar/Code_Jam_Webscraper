#include<bits/stdc++.h>

using namespace std;

#define X first
#define Y second
#define PB push_back
#define MP make_pair

int A[ 1445 ];

int main(){
	int T; cin >> T;
	for( int kase = 1; kase <= T; kase++ ){
		int Ac, Aj, c, d; cin >> Ac >> Aj;
		int Tc = 0, Tj = 0;
		for( int i = 0; i <= 1440; i++ ) 
			A[ i ] = 0;
		vector< int > v;
		for( int i = 0; i < Ac; i++ ){
			cin >> c >> d; Tc += (d-c);
			v.push_back( c );
			v.push_back( d );
			for( int j = c; j <= d; j++ ) 
				A[ j ] = 2;
		}
		for( int i = 0; i < Aj; i++ ){
			cin >> c >> d; Tj += (d-c);
			v.push_back( c );
			v.push_back( d );
			for( int j = c; j <= d; j++ )
				A[ j ] = 1;
		}
		//cout << Tc << " " << Tj << endl;
		int res = 0;
		if( Ac == Aj ) res = 2;
		else if( Ac + Aj == 1 ) res = 2;
		else{
			int ac = max( v[ 1 ], v[ 3 ] ) - min( v[ 0 ], v[ 2 ] );
			ac = min( ac, (1440-v[0])+v[3] );
			ac = min( ac, (1440-v[2])+v[1] );
			if( ac <= 720 ) res = 2;
			else res = 4;
		}
		cout << "Case #" << kase <<": " << res << endl;	
	}
}
