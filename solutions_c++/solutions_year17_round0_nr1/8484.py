#include <iostream>
#include <cstdio>
#include <queue>
#include <string.h>

using namespace std;

typedef pair< int, int > node;

int T, k, st, goal, sz;
bool visited[ (1 << 11) ];
string str;

int solve(){
	queue< node > q;
	q.push( make_pair( st, 0 ) );
	visited[ st ] = true;

	node cur;
	while( !q.empty() ){
		cur = q.front(); q.pop();
		if( cur.first == goal ) return cur.second;
		for( int i = 0; i + k <= sz; ++i ){
			int nState = cur.first;
			for( int j = i; j < i + k; ++j ) nState ^= (1 << j);
			if( !visited[ nState ] ){
				visited[ nState ] = 1;
				q.push( make_pair( nState, cur.second + 1 ) );
			}
		}

	}

	return -1;
}

int main(){

	ios_base::sync_with_stdio( 0 );
	cin.tie( 0 );

	freopen( "/home/vg/Programacion/input", "r", stdin );
	freopen( "/home/vg/Programacion/output", "w", stdout );

	cin >> T;

	for( int tc = 1; tc <= T; ++tc ){
		st = goal = 0;
		memset( visited, 0, sizeof( visited ) );
		cin >> str >> k;
		sz = str.size();

		for( int i = 0; i < sz; ++i ){
			if( str[ i ] == '+' ) st |= (1 << i);
			goal |= (1 << i);
		}

		int ans = solve();
		
		cout << "Case #" << tc << ": ";
		if( ans == -1 ) cout << "IMPOSSIBLE\n";
		else cout << ans << '\n';
	}

	return 0;
}