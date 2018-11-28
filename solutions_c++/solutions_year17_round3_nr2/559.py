#include <iostream>
#include <vector>
#include <algorithm>
#define P pair< int, int >
using namespace std;

struct interval{
	int a, b;
	int col;
	interval(){}
	interval( int _a, int _b, int _c ){
		a = _a, b = _b, col = _c;
	}
	bool operator < ( const interval& m ) const{
		return P( a, b ) < P( m.a, m.b );
	}
};

int dist( P a, P b ){
	if( b.first >= a.second )
		return b.first - a.second;
	return 24 * 60 - a.second + b.first;
}

int main()
{
	int test;
	int ac, aj;
	cin >> test;
	for( int T = 1; T <= test; T++ ){
		vector< int > A[2];
		vector< interval > all;
		int rem[2] = {12 * 60, 12 * 60};
		int C, J;
		cin >> C >> J;
		for( int i = 0; i < C; i++ ){
			int a, b;
			cin >> a >> b;
			rem[1] -= ( b - a );
			all.push_back( interval( a, b, 0 ) );
		}
		for( int i = 0; i < J; i++ ){
			int a, b;
			cin >> a >> b;
			rem[0] -= ( b - a );
			all.push_back( interval( a, b, 1 ) );
		}
		int res = 0;
		sort( all.begin(), all.end() );
		for( int i = 0; i < all.size(); i++ ){
			P p1 = P( all[i].a, all[i].b );
			P p2 = P( all[( i + 1 ) % all.size()].a, all[( i + 1 ) % all.size()].b );
			int ds = dist( p1, p2 );
			if( all[i].col != all[( i + 1 ) % all.size()].col )
				res++;
			else{
				A[all[i].col].push_back( ds );
				res += 2;
			}
		}
		//cerr << res << ' ' << rem[0] << ' ' << rem[1] << endl;
		for( int i = 0; i < 2; i++ ){
			sort( A[i].begin(), A[i].end() );
			for( int j = 0; j < A[i].size(); j++ )
				if( rem[1 - i] >= A[i][j] ){
					res -= 2;
					rem[1 - i] -= A[i][j];
				}
		}
		cout << "Case #" << T << ": " << res << endl;

	}
	return 0;
}