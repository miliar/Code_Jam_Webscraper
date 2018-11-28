#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <memory.h>
#include <math.h>
#include <assert.h>
#include <queue>
#include <map>
#include <set>
#include <string>
#include <algorithm>
#include <iostream>
#include <functional>

using namespace std;
typedef long long ll;
#define Fi first
#define Se second
#define pb(x) push_back(x)
#define sz(x) (int)x.size()
#define rep(i, n) for(int i=0;i<n;i++)
#define all(x) x.begin(), x.end()
typedef pair<int, int> pii;
typedef tuple<int, int, int> t3;
typedef pair<ll, ll> pll;
typedef pair<double, double> pdd;
typedef tuple<int, int, int, int> t4;

char S[55][55];
int n, m;
int num[55][55];

vector <int> E[5050], F[5050];
void add(int x, int y){
//	printf("E%d %d\n", x, y);
	E[x^1].pb(y);
	E[y^1].pb(x);
	F[y].pb(x^1);
	F[x].pb(y^1);
}

int xx[4] = {-1, 0, 1, 0};
int yy[4] = {0, 1, 0, -1};

int ok_dfs(int x, int y, int dir){
	if(x < 0 || y < 0 || x >= n || y >= m) return -1;
	if(S[x][y] == '-') return num[x][y] << 2 | dir;
	if(S[x][y] == '#') return -1;
	int ndir = dir;
	if(S[x][y] == '\\') ndir = 3 - dir;
	if(S[x][y] == '/') ndir = dir ^ 1;
	x += xx[ndir], y += yy[ndir];
	return ok_dfs(x, y, ndir);
}

int IMP;
int p[5050];
int chk[5050];
vector <int> v;
int Find(int x){
	return p[x] == x ? x : p[x] = Find(p[x]);
}

void dfs(int x){
	chk[x] = 1;
	for(int e : E[x]) if(chk[e] == 0) dfs(e);
	v.pb(x);
}

void dfs2(int x){
	chk[x] = 1;
	for(int e : F[x]) if(chk[e] == 0){
		p[Find(e)] = Find(x);
		dfs2(e);
	}
}

int ans[5050];
vector <int> ele[5050];

void Do(int N){
	v.clear();
	memset(chk, 0, sizeof chk);
	for(int i=0;i<N+N;i++) p[i] = i;
	for(int i=0;i<N+N;i++) if(chk[i] == 0) dfs(i);
	reverse(all(v));
	memset(chk, 0, sizeof chk);
	for(int i=0;i<N+N;i++){
		int e = v[i];
		if(chk[e] == 0) dfs2(e);
	}
	for(int i=0;i<N;i++){
		if(Find(i+i) == Find(i+i+1)){
			puts("IMPOSSIBLE");
			return;
		}
	}
	puts("POSSIBLE");
	memset(ans, 0, sizeof ans);
	
	rep(i, 5050)ele[i].clear();
	
	for(int i=0;i<N+N;i++) ele[Find(i)].pb(i);
	
	for(int i=0;i<N+N;i++)ans[i] = 1;
	
	for(int e : v)if(Find(e) == e){
		int chk = 0;
		for(int f : ele[e]){
			if(ans[f^1] == 0)chk = 1;
		}
		for(int f : ele[e]) ans[f] = chk;
	}
	for(int i=0;i<n;i++)rep(j, m) if(S[i][j] == '-'){
		if(ans[num[i][j] * 2]) S[i][j] = '|';
	}
	rep(i, n)printf("%s\n", S[i]);
}

void solve(){
	IMP = 0;
	scanf("%d%d", &n, &m);
	rep(i, n)scanf("%s", S[i]);
	rep(i, n)rep(j, m) num[i][j] = 0;
	int now = 0;
	rep(i, n)rep(j, m)if(S[i][j] == '-' || S[i][j] == '|'){
		S[i][j] = '-';
		num[i][j] = now++;
	}
	
	rep(i, n)rep(j, m){
		if(S[i][j] == '-'){
			int c = num[i][j];
			if(ok_dfs(i + xx[1], j + yy[1], 1) == -1 && ok_dfs(i + xx[3], j + yy[3], 3) == -1);
			else add(c<<1, c<<1);
			if(ok_dfs(i + xx[0], j + yy[0], 0) == -1 && ok_dfs(i + xx[2], j + yy[2], 2) == -1);
			else add(c<<1|1, c<<1|1);
		}
		else if(S[i][j] == '.'){
			S[i][j] = '-';
			num[i][j] = -10;
			int A[4] = {};
			rep(k, 4)A[k] = ok_dfs(i + xx[k], j + yy[k], k);
			
			pii a = pii(-1, -1);
			pii b = a;
			
			if(A[0] >= 0) a = pii(A[0] >> 2, (A[0] & 1));
			else if(A[2] >= 0) a = pii(A[2] >> 2, (A[2] & 1));
			if(A[1] >= 0) b = pii(A[1] >> 2, (A[1] & 1));
			else if(A[3] >= 0) b = pii(A[3] >> 2, (A[3] & 1));
			
			if(a.Fi == -1 && b.Fi == -1){
				IMP = 1;
			}
			else if(a.Fi == -1){
				add(b.Fi << 1 | b.Se, b.Fi << 1 | b.Se);
			}
			else if(b.Fi == -1){
				add(a.Fi << 1 | a.Se, a.Fi << 1 | a.Se);
			}
			else{
				add(a.Fi << 1 | a.Se, b.Fi << 1 | b.Se);
			}
			
			S[i][j] = '.'; num[i][j] = 0;
		}
	}
	
	if(IMP){
		puts("IMPOSSIBLE");
	}
	else{
		Do(now);
	}
	
	rep(i, 5050)E[i].clear(), F[i].clear();
}

int main(){
	int Tc = 1; scanf("%d", &Tc);
	for(int tc=1; tc<=Tc; tc++){
		printf("Case #%d: ", tc);
		solve();
	}
	return 0;
}

