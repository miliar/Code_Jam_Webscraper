#include <cstdio>
#include <cstring>
#include <cmath>
#include <vector>
#include <iostream>
#include <cstdlib>
#define maxn 209
using namespace std;
int n, m;
int a[maxn][maxn];
char s[maxn];
bool ban1[maxn][maxn], ban2[maxn][maxn];
vector<int>G[maxn];
int cx[maxn], ans[maxn][maxn];
bool vis[maxn];

bool in(int x, int y){
	return 1 <= x && x <= n && 1 <= y && y <= n;
}
void build_graph1(){
	for(int i = 1; i <= 2 * n; i++)
		G[i].clear();
		
	for(int i = 1 + 1 ; i <= 2 * n; i++){
		for(int j = 1 - n; j <= n - 1; j++){
			int x = (i + j) / 2;
			int y = (i - j) / 2;
			if(in(x, y) && x + y == i && x - y == j){
				if(ban1[x][y])
					continue;
				G[i].push_back(j + n);
			}
		}
	}
}

void build_graph2(){
	for(int i = 1; i <= 2 * n ;i++)
		G[i].clear();
	
	for(int i = 1; i <= n; i++){
		for(int j= 1; j <= n; j++){
			if(ban2[i][j])
				continue;
			G[i].push_back(j);
		}
	}	
}


bool dfs(int u){
	for(auto v : G[u]){
		if(vis[v])
			continue;
		vis[v] = 1;
		if(cx[v] == -1 || dfs(cx[v])){
			cx[v] = u;
			return 1;
		}
	}
	return 0;
}

void match(int n){
	memset(cx, -1, sizeof(cx));
	for(int i = 1; i <= n; i++){
		memset(vis, 0, sizeof(vis));
		dfs(i);
	}
}

void getans1(){
	for(int i = 1; i <= 2 * n; i++){
		if(cx[i] == -1)
			continue;
		int x = (i - n + cx[i]) / 2;
		int y = cx[i] - x;
		ans[x][y] += 1;
	}	
}

void getans2(){
	for(int i = 1; i <= n; i++){
		if(cx[i] == -1)
			continue;
		ans[cx[i]][i] += 2;
	}	
}

int main(){
	freopen("/Users/fengweiming/ProgramContest/GoogleCodeJam2017/QualificationRound/D.in", "r", stdin);
	freopen("/Users/fengweiming/ProgramContest/GoogleCodeJam2017/QualificationRound/DL.out", "w", stdout);
	int tt, cot = 1;
	scanf("%d", &tt);
	while(tt--){
		scanf("%d%d", &n, &m);
		memset(a, 0, sizeof(a));
		for(int i = 0; i < m; i++){
			int x, y;
			scanf("%s%d%d", s, &x, &y);
			if(s[0] == '+')
				a[x][y] = 1;
			else if(s[0] == 'x')
				a[x][y] = 2;
			else
				a[x][y] = 3;
		}
		
		memset(ban1, 0, sizeof(ban1));
		memset(ban2, 0, sizeof(ban2));
		for(int i = 1; i <= n; i++)
			for(int j = 1; j <= n; j++){
				if(a[i][j] == 1 || a[i][j] == 3){
					for(int k = 0; k <= n; k++){
						if(in(i + k, j + k))
							ban1[i + k][j + k] = 1;
						if(in(i - k, j - k))
							ban1[i - k][j - k] = 1;
						if(in(i + k, j - k))
							ban1[i + k][j - k] = 1;
						if(in(i - k, j + k))
							ban1[i - k][j + k] = 1;
					}
				}
				if(a[i][j] == 2 || a[i][j] == 3){
					for(int k = 0; k <= n; k++){
						if(in(i, j + k))
							ban2[i][j + k] = 1;
						if(in(i, j - k))
							ban2[i][j - k] = 1;
						if(in(i - k, j))
							ban2[i - k][j] = 1;
						if(in(i + k, j))
							ban2[i + k][j] = 1;
					}
				}
			}
		for(int i = 1; i <= n; i++)
			for(int j = 1; j <= n; j++)
				ans[i][j] = a[i][j];
		build_graph1();
		match(2 * n);
		getans1();
		build_graph2();
		match(n);
		getans2();
		
		int cnt = 0, sum = 0;
		for(int i = 1; i <= n; i++)
			for(int j = 1; j <= n; j++){
				if(ans[i][j] != a[i][j]){
					cnt++;
				}
				if(ans[i][j] == 1 || ans[i][j] == 2)
					sum++;
				if(ans[i][j] == 3)
					sum += 2;
		}
		printf("Case #%d: %d %d\n", cot++, sum, cnt);
		for(int i = 1; i <= n; i++){
			for(int j =1 ; j <= n; j++){
				if(ans[i][j] != a[i][j]){
					//printf("%d\n", ans[i][j]);
					if(ans[i][j] == 1)
						printf("+ %d %d\n", i ,j);
					else if(ans[i][j] == 2){
						printf("x %d %d\n", i , j);
					}
					else{
						printf("o %d %d\n", i, j);
					}
				}
			}
		}
		
	}
	return 0;
}
	