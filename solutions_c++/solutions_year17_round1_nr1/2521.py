#include <bits/stdc++.h>
using namespace std;

int T;
char grid[30][30];
int R, C;
int cas = 0;
char inside[30][30][30][30];
int dp[30][30][30][30];
void GetInside(int x1, int y1, int x2, int y2) {
	char c = '?';
	inside[x1][y1][x2][y2] = '?';
	for(int i = x1; i < x2; i++) {
		for(int j = y1; j < y2; j++) {
			if(grid[i][j] != '?') {
				if(c != '?') {
					if(c != grid[i][j]) {
						return;
					}
				} else c = grid[i][j];
			} 
		}
	}
	inside[x1][y1][x2][y2] = c;
}
int Code(int p, int d) {
	return p * 30 + d + 1;
}
void Decode(int& p, int& d, int code) {
	code--;
	d = code % 30;
	code /= 30;
	p = code;
}
int DP(int x1, int x2, int y1, int y2) {
	if(dp[x1][y1][x2][y2] == -2) return 0;
	if(dp[x1][y1][x2][y2]) return 1;
	if(inside[x1][y1][x2][y2] != '?') {
		dp[x1][y1][x2][y2] = -1;
		return 1;
	}
	dp[x1][y1][x2][y2] = -2;
	for(int p = x1 + 1; p < x2; p++) {
		if(DP(x1, p, y1, y2) && DP(p, x2, y1, y2)) {
			dp[x1][y1][x2][y2] = Code(p, 0);
			return 1;
		}
	}
	for(int p = y1 + 1; p < y2; p++) {
		if(DP(x1, x2, y1, p) && DP(x1, x2, p, y2)) {
			dp[x1][y1][x2][y2] = Code(p, 1);
			return 1;
		}
	}
	return 0;
}
char ans[30][30];
int vis[30][30][30][30];
void Print(int x1, int x2, int y1, int y2) {
	//if(vis[x1][y1][x2][y2]++) return;
	//printf("%d %d %d %d\n", x1, y1, x2, y2);
	if(dp[x1][y1][x2][y2] == -1) {
		for(int i = x1; i < x2; i++) {
			for(int j = y1; j < y2; j++) {
				ans[i][j] = inside[x1][y1][x2][y2];
			}
		}
		return;
	}
	int p, d;
	Decode(p, d, dp[x1][y1][x2][y2]);
	//cout << p << " " << d << endl;
	if(d == 0) {
		Print(x1, p, y1, y2);
		Print(p, x2, y1, y2);
	} else {
		Print(x1, x2, y1, p);
		Print(x1, x2, p, y2);
	}
}
int main() {
	freopen("./in.txt", "r", stdin);
	freopen("./out.txt", "w", stdout);
	cin >> T;
	while(T--) {
		memset(dp, 0, sizeof dp);
		memset(ans, 0, sizeof ans);
		printf("Case #%d:\n", ++cas);
		scanf("%d%d", &R, &C);
		for(int i = 0; i < R; i++) {
			scanf("%s", grid[i]);
		}
		for(int x1 = 0; x1 < R; x1++) {
			for(int x2 = x1 + 1; x2 <= R; x2++) {
				for(int y1 = 0; y1 < C; y1++) {
					for(int y2 = y1 + 1; y2 <= C; y2++) {
						GetInside(x1, y1, x2, y2);
						dp[x1][y1][x2][y2] = (inside[x1][y1][x2][y2] == '?' ? 0 : -1);
				//		printf("%d %d %d %d %c\n", x1, y1, x2, y2, inside[x1][y1][x2][y2]);
					}
				}
			}
		}
		DP(0, R, 0, C);
		for(int x1 = 0; x1 < R; x1++) {
			for(int x2 = x1 + 1; x2 <= R; x2++) {
				for(int y1 = 0; y1 < C; y1++) {
					for(int y2 = y1 + 1; y2 <= C; y2++) {
						//printf("%d %d %d %d %d\n", x1, y1, x2, y2, dp[x1][y1][x2][y2]);
					}
				}
			}
		}
		Print(0, R, 0, C);
		for(int i = 0; i < R; i++) {
			puts(ans[i]);
		}
	}
	return 0;
}
