#include <bits/stdc++.h>
using namespace std;

struct Rect {
	int si, sj, bi, bj;
	char ch;
};

bool ok ( vector<string>& G, const Rect r ) {
	if ( r.si < 0 || r.sj < 0 || r.bi >= G.size() || r.bj >= G[0].size() )
		return false;
	for ( int i = r.si; i <= r.bi; ++i )
		for ( int j = r.sj; j <= r.bj; ++j )
			if ( G[i][j] != '?' && G[i][j] != r.ch )
				return false;
	for ( int i = r.si; i <= r.bi; ++i )
		for ( int j = r.sj; j <= r.bj; ++j )
			G[i][j] = r.ch;
	return true;
}

inline int fastrand() { return rand(); }

int order[] = { 0, 1, 2, 3 };
vector<string> ans;

bool findSolution(vector<string> G, vector<Rect> rects ) {
	for ( int i = rects.size()-1; i > 0; --i )
		swap ( rects[i], rects[fastrand()%(i+1)] );
	
	for ( Rect r : rects ) {
		for ( int i = 3; i >= 0; --i )
			swap ( order[i], order[fastrand()%(i+1)] );
		for ( int x : order ) {
			if (x==0)      while(1) { r.si--; if ( ok(G,r) ) continue; r.si++; break; }
			else if (x==1) while(1) { r.bi++; if ( ok(G,r) ) continue; r.bi--; break; }
			else if (x==2) while(1) { r.sj--; if ( ok(G,r) ) continue; r.sj++; break; }
			else if (x==3) while(1) { r.bj++; if ( ok(G,r) ) continue; r.bj--; break; }
		}
	}
	
	for ( string& row : G )
		if ( row.find('?') != string::npos )
			return false;
		
	ans = G;
	return true;
}

void solve() {
	int h, w;
	cin >> h >> w;
	vector<string> G(h);
	for ( int i = 0; i < h; ++i )
		cin >> G[i];
	
	vector<Rect> rects;
	for ( char c = 'A'; c <= 'Z'; ++c )
	{
		Rect r;
		r.si = h, r.sj = w, r.bi = -1, r.bj = -1;
		for ( int i = 0; i < h; ++i )
			for ( int j = 0; j < w; ++j )
				if ( G[i][j] == c ) {
					r.si = min ( r.si, i );
					r.sj = min ( r.sj, j );
					r.bi = max ( r.bi, i );
					r.bj = max ( r.bj, j );
				}
		if ( r.si != h ) {
			r.ch = c;
			assert ( ok(G,r) );
			rects.push_back ( r );
		}
	}

	while ( !findSolution(G, rects) );
	
	for ( auto s : ans )
		cout << s << endl;
}

int main() {
	freopen ( "A-large.in", "r", stdin );
	freopen ( "A.out", "w", stdout );
	
	srand(time(0));
	
	int ntc;
	scanf ( "%d", &ntc );
	for ( int test = 1; test <= ntc; ++test ) {
		cout << "Case #" << test << ":\n";
		solve();
	}
	
	return 0;
}
