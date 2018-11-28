#include <bits/stdc++.h>
using namespace std;
typedef int ll;

#define MAX				101
int dist[MAX+1][MAX+1][MAX+1][MAX+1];

queue<ll> Q;

void add ( int a, int b, int c, int d, int w ) {
	if ( dist[a][b][c][d] == -1 ) {
		dist[a][b][c][d] = w;
		Q.push(a); Q.push(b); Q.push(c); Q.push(d);
	}
}

int solve() {
	ll H0, A0, H1, A1, B, D;
	cin >> H0 >> A0 >> H1 >> A1 >> B >> D;

	memset ( dist, -1, sizeof(dist) );
	while(!Q.empty()) Q.pop();
	add(H0,A0,H1,A1,0);
	
	while ( !Q.empty() ) {
		const int h0 = Q.front(); Q.pop();
		const int a0 = Q.front(); Q.pop();
		const int h1 = Q.front(); Q.pop();
		const int a1 = Q.front(); Q.pop();
		const int w = dist[h0][a0][h1][a1];
		
		if ( h0 == 0 ) continue;
		
		//attack and win :3
		if ( a0 >= h1 ) return w+1;
		
		//cure
		add ( max(H0-a1,0), a0, h1, a1, w+1 );
		
		//debuff
		add ( max(h0-max(a1-D,0),0), a0, h1, max(a1-D,0), w+1 );
		
		//buff
		add( max(h0-a1,0), min(MAX,a0+B), h1, a1, w+1 );
		
		//attack
		add( max(h0-a1,0), a0, max(h1-a0,0), a1, w+1 );
		
	}
	
	return -1;
}

int main() {
	freopen ( "C-small-attempt0.in", "r", stdin );
	freopen ( "C.out", "w", stdout );
	
	int ntc;
	scanf("%d", &ntc );
	for ( int test = 1; test <= ntc; ++test ) {
		int ans = solve();
		cout << "Case #" << test << ": ";
		if ( ans == -1 ) cout << "IMPOSSIBLE";
		else cout << ans;
		cout << endl;
	}
	
	return 0;
}
