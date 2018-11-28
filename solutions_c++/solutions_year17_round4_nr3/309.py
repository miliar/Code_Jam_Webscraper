#include <bits/stdc++.h>

#define FI(i,a,b) for(int i=(a);i<=(b);i++)
#define FD(i,a,b) for(int i=(a);i>=(b);i--)

#define LL long long
#define Ldouble long double
#define PI 3.1415926535897932384626

#define PII pair<int,int>
#define PLL pair<LL,LL>
#define mp make_pair
#define fi first
#define se second

using namespace std;

void fileIO(char in_name[20], char out_name[20]){
	char name[20];
	sprintf(name, "%s.in", in_name);
	freopen(name, "r", stdin);
	sprintf(name, "%s.out", out_name);
	freopen(name, "w", stdout);
}

int t, h, w;
char s[55][55];
bool poss[55][55][2];

struct config{
	int x, y, dir;
};

vector<config> sto[55][55];
bool vis[55][55];

int dx[4] = {0, 1, 0, -1};
int dy[4] = {1, 0, -1, 0};

int cg1[4] = {3, 2, 1, 0};
int cg2[4] = {1, 0, 3, 2};

bool boom;

void dfs(int cx, int cy, int dir){
	vis[cx][cy] = true;
	cx += dx[dir];
	cy += dy[dir];
	if(cx <= 0 || cx > h || cy <= 0 || cy > w) return;
	if(s[cx][cy] == '#') return;
	if(s[cx][cy] == '-'){
		boom = true;
		return;
	}
	if(s[cx][cy] == '/') dfs(cx, cy, cg1[dir]);
	else if(s[cx][cy] == '\\') dfs(cx, cy, cg2[dir]);
	else dfs(cx, cy, dir);
}

vector<config> edge[55][55][2];

int sol[55][55], jus[55][55];
int accept;

void gogogo(int cx, int cy){
	if(!accept) return;
	jus[cx][cy] = 1;
	for(auto cf: edge[cx][cy][sol[cx][cy]]){
		int nx = cf.x, ny = cf.y, ndir = cf.dir;
		if(sol[nx][ny] == -1){
			sol[nx][ny] = ndir;
			gogogo(nx, ny);
		}
		else if(sol[nx][ny] != ndir){
			accept = 0;
			return;
		}
	}
}

void solve(){
	memset(poss, 0, sizeof(poss));
	FI(i, 1, h) FI(j, 1, w) sto[i][j].clear();
	FI(i, 1, h) FI(j, 1, w) if(s[i][j] == '|') s[i][j] = '-';
	FI(i, 1, h) FI(j, 1, w) if(s[i][j] == '-'){
		FI(k, 0, 1){
			memset(vis, 0, sizeof(vis));
			boom = false;
			dfs(i, j, k);
			dfs(i, j, 2 + k);
			if(!boom){
				poss[i][j][k] = true;
				FI(i2, 1, h) FI(j2, 1, w){
					if((i == i2 && j == j2) || (vis[i2][j2] && s[i2][j2] == '.')){
						sto[i2][j2].push_back((config){i, j, k});
					}
				}
			}
		}
	}
	/*
	FI(i, 1, h) FI(j, 1, w){
		for(auto cf: sto[i][j]){
			printf("%d %d: have %d %d %d\n", i, j, cf.x, cf.y, cf.dir);
		}
	}
	*/
	memset(sol, -1, sizeof(sol));
	FI(i, 1, h) FI(j, 1, w) FI(k, 0, 1) edge[i][j][k].clear();
	FI(i, 1, h) FI(j, 1, w) if(s[i][j] == '.' || s[i][j] == '-'){
		int sz = sto[i][j].size();
		if(sz == 0){
			printf("IMPOSSIBLE\n");
			return;
		}
		else if(sz == 1){
			//fixed
			int cur = sol[sto[i][j][0].x][sto[i][j][0].y];
			int tar = sto[i][j][0].dir;
			if(cur == 1 - tar){
				printf("IMPOSSIBLE\n");
				return;
			}
			sol[sto[i][j][0].x][sto[i][j][0].y] = tar;
		}
		else{
			assert(sz == 2);
			config A = sto[i][j][0];
			config B = sto[i][j][1];
			edge[A.x][A.y][1 - A.dir].push_back(B);
			edge[B.x][B.y][1 - B.dir].push_back(A);
		}
	}
	
	FI(i, 1, h) FI(j, 1, w) if(s[i][j] == '-'){
		if(sol[i][j] == -1){
			sol[i][j] = 0;
			memset(jus, 0, sizeof(jus));
			accept = 1;
			gogogo(i, j);
			if(!accept){
				FI(i2, 1, h) FI(j2, 1, w){
					if(jus[i2][j2]) sol[i2][j2] = -1;
				}
				sol[i][j] = 0;
				accept = 1;
				gogogo(i, j);
				if(!accept){
					printf("IMPOSSIBLE\n");
					return;
				}
			}
		}
	}
	printf("POSSIBLE\n");
	FI(i, 1, h) FI(j, 1, w) if(s[i][j] == '-'){
		if(sol[i][j] == 1) s[i][j] = '|';
	}
	FI(i, 1, h) printf("%s\n", s[i] + 1);
}

int main(){
	fileIO("C-small-attempt0", "C1");
	scanf("%d", &t);
	FI(i, 1, t){
		printf("Case #%d: ", i);
		scanf("%d %d", &h, &w);
		FI(j, 1, h) scanf(" %s", s[j] + 1);
		solve();
	}
	return 0;
}

