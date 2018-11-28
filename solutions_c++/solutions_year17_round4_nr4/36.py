#include <bits/stdc++.h>

using namespace std;

const int MX = 100;
const int dx[] = {1, -1,  0, 0};
const int dy[] = {0,  0, -1, 1};

char S[MX][MX + 1];
bool bad[MX][MX], vis[MX][MX];

char s[MX][MX + 1];
int sx[MX], sy[MX], tx[MX], ty[MX], n, p;
bool f[1 << 10][10][10], dp[1 << 10][1 << 10];

void print(int i, int j) {
	if (i == 0) return;
	
	for (int x = 0; x < n; x++)
		if ((i >> x) & 1)
			for (int y = 0; y < p; y++)
				if ((j >> y) & 1)
					if (dp[i ^ (1 << x)][j ^ (1 << y)] && f[j ^ (1 << y)][x][y]) {
						print(i ^ (1 << x), j ^ (1 << y));
						printf("%d %d\n", x + 1, y + 1);
						return;
					}
	
}

int main() {
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		memset(f, 0, sizeof f);
		memset(dp, 0, sizeof dp);
		
		int c, r, m;
		n = p = 0;
		scanf("%d %d %d", &c, &r, &m);
		for (int i = 0; i < r; i++) scanf(" %s", s[i]);
		
		for (int i = 0; i < r; i++)
			for (int j = 0; j < c; j++) {
				if (s[i][j] == 'S') {
					sx[n] = i;
					sy[n] = j;
					n++;
				}
				
				if (s[i][j] == 'T') {
					tx[p] = i;
					ty[p] = j;
					p++;
				}
			}
		
		for (int msk = 0; msk < (1 << p); msk++) {
			memcpy(S, s, sizeof S);
			memset(bad, 0, sizeof bad);
			
			for (int i = 0; i < p; i++) {
				if ((msk >> i) & 1) S[tx[i]][ty[i]] = '.';
				else {
					for (int dir = 0; dir < 4; dir++) {
						int x = tx[i], y = ty[i];
						while (true) {
							if (x < 0 || x == r || y < 0 || y == c) break;
							if (S[x][y] == '#') break;
							
							bad[x][y] = true;
							x += dx[dir];
							y += dy[dir];
						}
					}
				}
			}
			
			for (int i = 0; i < n; i++) {
				memset(vis, 0, sizeof vis);
				
				vector<tuple<int, int, int>> q = {make_tuple(sx[i], sy[i], 0)};
				vis[sx[i]][sy[i]] = true;
				for (size_t j = 0; j < q.size(); j++) {
					int x, y, d;
					tie(x, y, d) = q[j];
					
					if (bad[x][y] || d == m) continue;
					
					for (int dir = 0; dir < 4; dir++) {
						int xx = x + dx[dir];
						int yy = y + dy[dir];
						if (xx < 0 || xx == r || yy < 0 || yy == c) continue;
						if (S[xx][yy] == '#' || S[xx][yy] == 'T') continue;
						if (vis[xx][yy]) continue;
						
						vis[xx][yy] = true;
						q.emplace_back(xx, yy, d + 1);
					}
				}
				
				for (int j = 0; j < p; j++) {
					if ((msk >> j) & 1) continue;
					
					for (int dir = 0; dir < 4; dir++) {
						int x = tx[j], y = ty[j];
						while (true) {
							if (x < 0 || x == r || y < 0 || y == c) break;
							if (S[x][y] == '#') break;
							
							if (vis[x][y]) f[msk][i][j] = true;
							
							x += dx[dir];
							y += dy[dir];
						}
					}
					
//					printf("\tf(%d, %d, %d) = %d\n", msk, i, j, f[msk][i][j] ? 1 : 0);
				}
			}
		}
		
		int besti = 0, bestj = 0;
		
		dp[0][0] = true;
		for (int i = 1; i < (1 << n); i++)
			for (int j = 1; j < (1 << p); j++)
				if (__builtin_popcount(i) == __builtin_popcount(j)) {
					dp[i][j] = false;
					for (int x = 0; x < n; x++)
						if ((i >> x) & 1)
							for (int y = 0; y < p; y++)
								if ((j >> y) & 1)
									dp[i][j] = dp[i][j] || (dp[i ^ (1 << x)][j ^ (1 << y)] && f[j ^ (1 << y)][x][y]);
					
					if (dp[i][j] && __builtin_popcount(i) > __builtin_popcount(besti)) {
						besti = i;
						bestj = j;
					}
					
//					printf("\tdp(%d, %d) = %d\n", i, j, dp[i][j] ? 1 : 0);
				}
		
		printf("Case #%d: %d\n", t, (int)__builtin_popcount(besti));
		print(besti, bestj);
	}

	return 0;
}
