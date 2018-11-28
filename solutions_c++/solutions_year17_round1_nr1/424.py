#include <bits/stdc++.h>
using namespace std;

const int dx[5] = {1, -1, 0, 0};
const int dy[5] = {0, 0, 1, -1};
const int maxn = 55;
char G[maxn][maxn];
int n, m;
bool vis[maxn][maxn];

int main() {
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	int T, _ = 1;
	scanf("%d", &T);
	while(T--) {
		scanf("%d %d", &n, &m);
		memset(G, 0, sizeof(G));
		memset(vis, 0, sizeof(vis));
		for(int i = 0; i < n; i++) {
			scanf("%s", G[i]);
		}
	  for(int i = 0; i < n; i++) {
	  	for(int j = 0; j < m; j++) {
	  		if(G[i][j] == '?') {
	  			vis[i][j] = 1;
	  		}
	  	}
	  }
		for(int i = 0; i < n; i++) {
			for(int j = 0; j < m; j++) {
				if(vis[i][j]) continue;
				bool flag = 0;
				for(int k = j+1; k < m; k++) {
					if(G[i][k] == '?') {
						G[i][k] = G[i][j];
						flag = 1;
					}
					else break;
				}
				for(int k = j-1; k >= 0; k--) {
					if(G[i][k] == '?') {
						G[i][k] = G[i][j];
						flag = 1;
					}
					else break;
				}
				if(!flag) {
					for(int k = i+1; k < n; k++) {
						if(G[k][j] == '?') G[k][j] = G[i][j];
						else break;
					}
					for(int k = i-1; k >= 0; k--) {
						if(G[k][j] == '?') G[k][j] = G[i][j];
						else break;
					}
				}
			}
		}
		int ok = 1;
		while(1) {
			for(int i = 0; i < n; i++) {
				for(int j = 0; j < m; j++) {
					if(G[i][j] == '?') {
						ok = 0;
						for(int k = 0; k < 4; k++) {
							int x = i + dx[k];
							int y = j + dy[k];
							if(G[x][y]!='?'&&x>=0&&x<n&&y>=0&&y<m) {
								G[i][j] = G[x][y];
								break;
							}
						}
					}
				}
			}
			if(ok) break;
			ok = 1;
		}
		printf("Case #%d:\n", _++);
		for(int i = 0; i < n; i++) {
			cout << G[i] << endl;
		}
	}
	return 0;
}
