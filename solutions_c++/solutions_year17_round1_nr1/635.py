#include <iostream>
#include <cstdio>
#include <cstdlib>

using namespace std;

int n, m;
char s[101];
int map[101][101];

void solvecol(int x){
	int l, r;
	for(int i = 1; i <= n; ++i){
		if(map[i][x] != 0){
			l = i - 1;
			while(l > 0 && map[l][x] == 0){
				map[l][x] = map[i][x];
				--l;
			}
			r = i + 1;
			while(r <= n && map[r][x] == 0){
				map[r][x] = map[i][x];
				++r;
			}
		}
	}
}

void solverow(int x){
	if(map[1][x] != 0)
		return;
	for(int i = x - 1; i > 0; --i){
		if(map[1][i] != 0){
			for(int j = 1; j <= n; ++j)
				map[j][x] = map[j][i];
			return;
		}
	}
	for(int i = x + 1; i <= m; ++i){
		if(map[1][i] != 0){
			for(int j = 1; j <= n; ++j)
				map[j][x] = map[j][i];
			return;
		}
	}
}

void work(){
	for(int i = 1; i <= m; ++i) 
		solvecol(i);
	for(int i = 1; i <= m; ++i)
		solverow(i);
	for(int i = 1; i <= n; ++i){
		for(int j = 1; j <= m; ++j){
			printf("%c", map[i][j]);
		}
		printf("\n");
	}
}

int main(){
	freopen("A-large.in", "r", stdin);
	freopen("A.out", "w", stdout);
	int T;
	cin >> T;
	for(int t = 1; t <= T; ++t){
		scanf("%d%d", &n, &m);
		for(int i = 1; i <= n; ++i){
			scanf("%s", s + 1);
			for(int j = 1; j <= m; ++j){
				if(s[j] == '?') map[i][j] = 0;
				else map[i][j] = s[j];
			}
		}
		printf("Case #%d:\n", t);
		work();
	}
	return 0;
}
