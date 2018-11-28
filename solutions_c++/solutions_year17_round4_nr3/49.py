#include<stdio.h>
#include<assert.h>
#include<cmath>
#include<algorithm>
#include<iostream>
#include<vector>
#include<string>
#include<cmath>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef pair<double, double> pdd;
typedef pair<double, int> pdi;

const double EPS = 1e-8;
const double PI = acos(-1);

int solve();

int main()
{
	int T;
	scanf("%d", &T);
	for(int t = 1; t <= T; t++){
		printf("Case #%d: ", t);
		solve();
	}
}

const int MX = 405;

char D[MX][MX];
int ad[MX][MX];

vector<int> G[MX], R[MX], T[MX];
int t = 0, N, M;

void make_edge(int a, int b){
	G[a].push_back(b); G[b^1].push_back(a^1);
	R[b].push_back(a); R[a^1].push_back(b^1);
}

void dfs1(int x, int vst[MX], vector<int> &L){
	if( vst[x] ) return;
	vst[x] = 1;
	for(int c : G[x]) dfs1(c, vst, L);
	L.push_back(x);
}

void dfs2(int x, int cur, vector<int> &C, int ad[MX])
{
	ad[x] = cur;
	C.push_back(x);
	for(int c : R[x]){
		int p = ad[c];
		if( p == cur );
		else if( p && (!T[p].size() || T[p].back() != cur)) T[p].push_back(cur);
		else if( !p ) dfs2(c, cur, C, ad);
	}
}

bool _2SAT(int N, int ans[MX]){
	fprintf(stderr, "%d\n", N*2);
	static int vst[MX], ad[MX], cur = 0;
	vector<int> L;
	vector<int> C[MX];
	
	for(int i = 0; i < MX; i++) vst[i] = ad[i] = 0;
	cur = 0;
	for(int i = 0; i < N*2; i++) dfs1(i, vst, L);
	reverse(L.begin(), L.end());
	for(int c : L){
		if( !ad[c] ) cur++, dfs2(c, cur, C[cur], ad);
	}

	for(int i = 0; i < N; i++) ans[i] = -1;
	for(int i = 0; i < N; i++) if( ad[i*2] == ad[i*2+1] ) return false;
	for(int i = 1; i <= cur; i++){
		for(int c : C[i]){
			int d = c/2;
			if( ans[d] == -1 ) ans[d] = ~c&1;
		}
	}
	return true;
}

int dx[4] = {-1, 0, 1, 0};
int dy[4] = {0, 1, 0, -1};
int trace(int x, int y, int d){
	if( x < 0 || x >= N || y < 0 || y >= M ) return 0;
	x += dx[d], y += dy[d];
	if( x < 0 || x >= N || y < 0 || y >= M ) return 0;
	if( D[x][y] == '/' ) d ^= 1;
	else if( D[x][y] == '\\') d ^= 3;
	else if( D[x][y] == '#' ) return 0;
	else if( D[x][y] == '-' || D[x][y] == '|' ) return ad[x][y] * 2 + (d&1);
	return trace(x, y, d);
}

int solve()
{
	scanf("%d%d", &N, &M);
	for(int i = 0; i < N; i++) scanf("%s", D[i]);
	for(int i = 0; i < N; i++) for(int j = 0; j < M; j++) ad[i][j] = 0;

	t = 0;
	for(int i = 0; i < N; i++){
		for(int j = 0; j < M; j++){
			if( D[i][j] == '-' || D[i][j] == '|' ) ad[i][j] = ++t;
		}
	}
	for(int i = 0; i < MX; i++) G[i].clear(), R[i].clear(), T[i].clear();

	make_edge(0, 1);
	for(int i = 0; i < N; i++){
		for(int j = 0; j < M; j++){
			if( !ad[i][j] ) continue;
			int c = ad[i][j];
			int n[4];
			for(int d = 0; d < 4; d++) n[d] = trace(i, j, d);
			if( n[0] ) make_edge(1, n[0]^1), make_edge(1, c*2+1);
			if( n[1] ) make_edge(1, n[1]^1), make_edge(1, c*2);
			if( n[2] ) make_edge(1, n[2]^1), make_edge(1, c*2+1);
			if( n[3] ) make_edge(1, n[3]^1), make_edge(1, c*2);
		}
	}
	for(int i = 0; i < N; i++){
		for(int j = 0; j < M; j++){
			if( D[i][j] != '.' ) continue;
			int n[4];
			for(int d = 0; d < 4; d++) n[d] = trace(i, j, d);
			if( n[0] == 0 ) swap(n[0], n[2]);
			if( n[1] == 0 ) swap(n[1], n[3]);

			bool ch = 0;
			int a = 0, b = 0;
			if( n[0] && !n[2] )	a = n[0];
			if( n[1] && !n[3] ) b = n[1];
			make_edge(a^1, b);
		}
	}
	int ans[MX] = {};
	if( !_2SAT(t+1, ans) ){
		return !printf("IMPOSSIBLE\n");
	}
	printf("POSSIBLE\n");
	for(int i = 0; i < N; i++){
		for(int j = 0; j < M; j++){
			if( !ad[i][j] ) continue;
			if( ans[ad[i][j]] == 1 ) D[i][j] = '-';
			else D[i][j] = '|';
		}
	}
	for(int i = 0; i < N; i++){
		printf("%s\n", D[i]);
	}
}
