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
#include <unordered_map>
#include <unordered_set>
#include <list>
#include <bitset>

using namespace std;
typedef pair<int, int> Pi;
typedef long long ll;
#define pii Pi
#define pll PL
#define Fi first
#define Se second
#define pb(x) push_back(x)
#define sz(x) ((int)(x).size())
#define rep(i, n) for(int i=0;i<n;i++)
#define all(x) (x).begin(), (x).end()
typedef tuple<int, int, int> t3;
typedef pair<ll, ll> PL;
typedef long double ldouble;

char P[110][110], Q[110][110];
vector <int> E[210];
int yx[210], vis[210];

int dfs(int x){
	vis[x] = 1;
	for(int e : E[x])if(yx[e] == 0 || (vis[yx[e]] == 0 && dfs(yx[e]))){
		yx[e] = x;
		return 1;
	}
	return 0;
}

void solve(){
	int n, m;
	scanf("%d%d", &n, &m);
	memset(P, 0, sizeof P);
	memset(Q, 0, sizeof Q);
	int chk_x[2][110] = {};
	int chk_y[2][220] = {};	//0 : x+y-1, 1 : x-y+n
	rep(i, m){
		char ch[2];
		int x, y;
		scanf("%s%d%d", ch, &x, &y);
		Q[x][y] = P[x][y] = ch[0];
		if(ch[0] != '+')chk_x[0][x] = chk_x[1][y] = 1;
		if(ch[0] != 'x')chk_y[0][x+y-1] = chk_y[1][x-y+n] = 1;
	}
	for(int i=1;i<=n;i++)E[i].clear(), yx[i] = 0;
	for(int i=1;i<=n;i++){
		for(int j=1;j<=n;j++){
			if(chk_x[0][i] == 0 && chk_x[1][j] == 0){
				E[i].pb(j);
			}
		}
	}
	for(int i=1;i<=n;i++){
		for(int j=1;j<=n;j++)vis[j] = 0;
		dfs(i);
	}
	for(int i=1;i<=n;i++){
		if(yx[i] > 0){
			Q[yx[i]][i] = (Q[yx[i]][i] == '+' ? 'o' : 'x');
		}
	}
	for(int i=1;i<n*2;i++)E[i].clear(), yx[i] = 0;
	for(int i=1;i<=n;i++){
		for(int j=1;j<=n;j++){
			if(chk_y[0][i+j-1] == 0 && chk_y[1][i-j+n] == 0){
				E[i+j-1].pb(i-j+n);
			}
		}
	}
	for(int i=1;i<n*2;i++){
		for(int j=1;j<n*2;j++)vis[j] = 0;
		dfs(i);
	}
	for(int i=1;i<n*2;i++){
		if(yx[i] > 0){
			int tx = yx[i], ty = i;
			int x = (tx + ty + 1 - n) / 2;
			int y = tx + 1 - x;
			Q[x][y] = (Q[x][y] == 'x' ? 'o' : '+');
		}
	}
	int ans = 0, dcnt = 0;
	for(int i=1;i<=n;i++)for(int j=1;j<=n;j++){
		if(Q[i][j])ans++;
		if(Q[i][j] == 'o')ans++;
		if(Q[i][j] != P[i][j])dcnt++;
	}
	printf("%d %d\n", ans, dcnt);
	for(int i=1;i<=n;i++)for(int j=1;j<=n;j++)if(P[i][j] != Q[i][j]){
		printf("%c %d %d\n", Q[i][j], i, j);
	}
}

int main(){
	int Tc = 1; scanf("%d\n", &Tc);
	for(int tc=1;tc<=Tc;tc++){
		printf("Case #%d: ", tc);
		solve();
	}
}
