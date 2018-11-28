#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#define P pair< int, int >

using namespace std;

struct node{
	P p;
	int v1, v2;
	bool operator < ( const node& m ) const{
		if( v1 != m.v1 )
			return v1 > m.v1;
		if( v2 != m.v2 )
			return v2 > m.v2;
		return p < m.p;
	}
	node(){}
	node( P _p, int _v1, int _v2 ){
		p = _p;
		v1 = _v1;
		v2 = _v2;
	}
};

int getV1( P p ){
	int mid = ( p.first + p.second ) / 2;
	return min( mid - p.first, p.second - mid );
}

int getV2( P p ){
	int mid = ( p.first + p.second ) / 2;
	return max( mid - p.first, p.second - mid );
}

int main()
{
	int test;
	cin >> test;
	for( int T = 1; T <= test; T++ ){
		int n, k;
		cin >> n >> k;
		P res;
		vector< node > lev[30];
		lev[0].push_back( node( P( 1, n + 2 ), getV1( P( 1, n + 2 ) ), getV2( P( 1, n + 2 ) ) ) );
		int cnt = 0, curLev = 0;
		while( cnt < k ){
			set< node > st;
			int sz = lev[curLev].size();
			for( int i = 0; cnt < k && i < sz; i++ ){
				node m = lev[curLev][i];
				int mid = ( m.p.first + m.p.second ) / 2;
				P l( m.p.first, mid );
				P r( mid, m.p.second );
				lev[curLev].push_back( node( l, getV1( l ), getV2( l ) ) );
				lev[curLev].push_back( node( r, getV1( r ), getV2( r ) ) );
				st.insert( m );
			}
			sort( lev[curLev].begin(), lev[curLev].end() );
			for( int i = 0; cnt < k && i < lev[curLev].size(); i++ ){
				node m = lev[curLev][i];
				//cout << m.p.first << ' ' << m.p.second << endl;
				int mid = ( m.p.first + m.p.second ) / 2;
				cnt++;
				if( cnt == k )
					res = P( max( mid - m.p.first, m.p.second - mid ), min( mid - m.p.first, m.p.second - mid ) );
				if( st.count( m ) == 0 ){
					P l( m.p.first, mid );
					P r( mid, m.p.second );
					lev[curLev + 1].push_back( node( l, getV1( l ), getV2( l ) ) );
					lev[curLev + 1].push_back( node( r, getV1( r ), getV2( r ) ) );
				}
			}
			curLev++;
		}
		cout << "Case #" << T << ": ";
		cout << res.first - 1 << ' ' << res.second - 1 << endl;
	}
	return 0;
}