#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
#include <queue>
#include <set>
#include <map>
#include <sstream>
#include <iomanip>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <ctime>
#include <cassert>
#include <windows.h>
using namespace std;
typedef long long ll;
typedef double R;
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define FOR(i, s, t) for(i = (s); i < (t); i++)
#define RFOR(i, s, t) for(i = (s)-1; i >= (t); i--)

const R PI = acos(-1);
const int MAXN = 61;
const int P = 1e9+7;

const int dx[] = {0, 1, 0, -1};
const int dy[] = {1, 0, -1, 0};

char s[MAXN][MAXN];
int x[MAXN*MAXN], y[MAXN*MAXN];
pair<int, int> to[MAXN][MAXN];
int cnt[MAXN][MAXN];
bool vis[MAXN][MAXN][4];
bool bad;

int n, m, ns;

bool isVis(int i, int j){
	return s[i][j] != '#' && (vis[i][j][0] || vis[i][j][1] || vis[i][j][2] || vis[i][j][3]);
}

void dfs(int i, int j, int d, bool conflict = true){
	if(vis[i][j][d])
		return;
	vis[i][j][d] = true;
	if(conflict && (s[i][j] == '|' || s[i][j] == '-')){
		bad = true;
		return;
	}
	if(s[i][j] == '#')
		return;
	if(s[i][j] == '/'){
		d = 3-d;
	}
	if(s[i][j] == '\\'){
		d ^= 1;
	}
	dfs(i+dx[d], j+dy[d], d);
}

vector<pair<int, int> > e[MAXN*MAXN][2];

void add(int i1, int j1, int i2, int j2){
	e[i1][j1^1].pb(mp(i2, j2));
	e[i2][j2^1].pb(mp(i1, j1));
}

namespace SAT{
	int &n = ns;
	bool vis[MAXN*MAXN][2];
	int ans[MAXN*MAXN];
	int q[MAXN*MAXN];
	int h, t;

	void dfs(int i, int j){
		if(vis[i][j])
			return;
		vis[i][j] = true;
		for(pair<int, int> &p : e[i][j]){
			dfs(p.fi, p.se);
		}
	}

	void clear_queue(){
		while(h < t){
			int i = q[h++];
			memset(vis, 0, sizeof vis);
			dfs(i, ans[i]);
			for(int j = 0; j < n; j++)
				if(ans[j] == -1 && (vis[j][0] || vis[j][1])){
					ans[j] = !vis[j][0];
					q[t++] = j;
				}
		}
	}

	bool solve(){
		int i, j;
		h = t = 0;
		memset(ans, -1, sizeof ans);
		for(i = 0; i < n; i++){
			for(j = 0; j < 2; j++){
				memset(vis, 0, sizeof vis);
				dfs(i, j);
				if(vis[i][j^1]){
					if(ans[i] == j)
						return false;
					if(ans[i] == -1){
						ans[i] = j^1;
						q[t++] = i;
					}
				}
			}
		}
		clear_queue();
		for(i = 0; i < n; i++)
			if(ans[i] == -1){
				ans[i] = 0;
				q[t++] = i;
				clear_queue();
			}
		return true;
	}
}

void print_cover(){
	for(int i = 1; i <= n; i++, puts(""))
		for(int j = 1; j <= m; j++)
			printf("%d", isVis(i, j));
}

int main(){
	//freopen("C-small-attempt0.in", "r", stdin);
	freopen("out.txt", "w", stdout);

	int T, i0;
	scanf("%d", &T);
	for(i0 = 1; i0 <= T; i0++){
		fflush(stdout);
		int i, j, k;
		ns = 0;
		scanf("%d%d", &n, &m);
		for(i = 1; i <= n; i++)
			scanf("%s", s[i]+1);
		for(i = 0; i <= n+1; i++)
			s[i][0] = s[i][m+1] = '#';
		for(j = 0; j <= m+1; j++)
			s[0][j] = s[n+1][j] = '#';

		for(i = 1; i <= n; i++)
			for(j = 1; j <= m; j++)
				if(s[i][j] == '|' || s[i][j] == '-'){
					x[ns] = i;
					y[ns] = j;
					ns++;
				}
		for(i = 0; i < ns; i++){
			e[i][0].clear();
			e[i][1].clear();
		}
		memset(to, -1, sizeof to);
		memset(cnt, 0, sizeof cnt);
		for(k = 0; k < ns; k++){
			memset(vis, 0, sizeof vis);
			bad = false;
			dfs(x[k], y[k], 0, false);
			dfs(x[k], y[k], 2, false);
			if(!bad){
				for(i = 1; i <= n; i++)
					for(j = 1; j <= m; j++)
						if(s[i][j] != '#' && isVis(i, j)){
							if(to[i][j].fi == -1)
								to[i][j] = mp(k, 0);
							else{
								add(k, 0, to[i][j].fi, to[i][j].se);
							}
							cnt[i][j]++;
						}
			}
#ifdef TT
			printf("%d %d %d 0 (bad=%d)\n", k, x[k], y[k], bad);
			print_cover();
#endif
			bool bad1 = bad;


			memset(vis, 0, sizeof vis);
			bad = false;
			dfs(x[k], y[k], 1, false);
			dfs(x[k], y[k], 3, false);
			if(bad1 && bad)
				goto no_solution;
			if(!bad){
				for(i = 1; i <= n; i++)
					for(j = 1; j <= m; j++)
						if(s[i][j] != '#' && isVis(i, j)){
							if(to[i][j].fi == -1)
								to[i][j] = mp(k, 1);
							else{
								add(k, 1, to[i][j].fi, to[i][j].se);
							}
							cnt[i][j]++;
						}
			}
#ifdef TT
			printf("%d %d %d 1 (bad=%d)\n", k, x[k], y[k], bad);
			print_cover();
#endif
		}
		for(i = 1; i <= n; i++)
			for(j = 1; j <= m; j++)
					if(s[i][j] != '#'){
						if(cnt[i][j] == 0)
							goto no_solution;
						if(cnt[i][j] == 1)
							add(to[i][j].fi, to[i][j].se, to[i][j].fi, to[i][j].se);
					}
//		if(i0 == 4)
//			printf("!!!!!!!!!!!!!%d %d %d\n", cnt[2][3], to[2][3].fi, to[2][3].se);
		if(SAT::solve()){
			printf("Case #%d: POSSIBLE\n", i0);
			for(i = 0; i < ns; i++)
				s[x[i]][y[i]] = SAT::ans[i] ? '|' : '-';
			for(i = 1; i <= n; i++){
				s[i][m+1] = 0;
				puts(s[i]+1);
			}
			continue;
		}
		no_solution:
		printf("Case #%d: IMPOSSIBLE\n", i0);
	}
	return 0;
}
