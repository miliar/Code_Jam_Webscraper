#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <map>
#include <set>
#include <queue>
#define eps 1e-8
#define MAXN 100050
#define LL long long
using namespace std;
char a[111][111];
char s[111][111];
bool bc[1111], br[1111];
bool dl[1111], dr[1111];
int ansc[11111], ansx[11111], ansy[11111];
int idl[111][111], idr[111][111];

bool g[222][222];
bool marky[222];
int linky[222];
bool find(int x, int n) {
	for (int y = 0; y < n; y++)
		if (g[x][y] && !marky[y]) {
			marky[y] = true;
			if (linky[y] == -1 || find(linky[y], n)) {
				linky[y] = x;
				return true;
			}
		}
	return false;
}

int erfen(int n) {
	memset(linky, -1, sizeof(linky));
	int ans = 0;
	for (int i = 0; i < n; i++) {
		memset(marky, false, sizeof(marky));
		if (find(i, n))
			ans++;
	}
	return ans;
}

int main() {
	freopen("D-large.in", "r", stdin);
	freopen("D-large.out", "w", stdout);
	int tt, ri = 0;
	scanf("%d", &tt);
	int ans;
	while (tt--) {
		int n, m;
		int tail = 0;
		scanf("%d%d", &n, &m);
		memset(a, 0, sizeof(a));
		memset(s, 0, sizeof(s));
		memset(bc, 0, sizeof(bc));
		memset(br, 0, sizeof(br));
		memset(dl, 0, sizeof(dl));
		memset(dr, 0, sizeof(dr));
		for (int i = 1; i <= n; ++i) {
			int x, y;
			x = n - i + 1, y = 1;
			while (x <= n) {
				idr[x][y] = i * 2 - 1;
				x++;
				y++;
			}

			x = 1, y = i;
			while (y > 0) {
				idl[x][y] = i * 2 - 1;
				x++;
				y--;
			}

			if (i == n)
				continue;
			x = 1, y = n - i + 1;
			while (y <= n) {
				idr[x][y] = i * 2;
				x++;
				y++;
			}

			x = n - i + 1, y = n;
			while (x <= n) {
				idl[x][y] = i * 2;
				x++;
				y--;
			}
		}
		ans = 0;
		for (int i = 0; i < m; ++i) {
			char ch;
			int l, r;
			scanf(" %c%d%d", &ch, &l, &r);
			a[l][r] = s[l][r] = ch;
			if (ch == 'o' || ch == '+') {
				dl[idl[l][r]] = true;
				dr[idr[l][r]] = true;
				ans++;
			}
			if (ch == 'o' || ch == 'x') {
				br[l] = true;
				bc[r] = true;
			}
		}
		memset(g, 0, sizeof(g));
		for (int i = 1; i <= n; ++i) {
			for (int j = 1; j <= n; ++j) {
				if (dl[idl[i][j]] || dr[idr[i][j]])
					continue;
				g[idl[i][j]][idr[i][j]] = 1;
			}
		}
		ans += erfen(n * 2);
		ans += n;
		for (int i = 1; i < n * 2; ++i) {
			if (linky[i] != -1) {
				int xx = linky[i], yy = i;
				for (int u = 1; u <= n; ++u) {
					for (int v = 1; v <= n; ++v) {
						if (idl[u][v] == xx && idr[u][v] == yy) {
							if (s[u][v] == 'x')
								s[u][v] = 'o';
							else
								s[u][v] = '+';
							//	printf("id:%d %d\n",idl[u][v],idr[u][v]);
						}
					}
				}
			}
		}
		for (int i = 1; i <= n; ++i) {
			if (br[i] == true)
				continue;
			for (int j = 1; j <= n; ++j) {
				if (bc[j] == true)
					continue;
				if (s[i][j] == '+')
					s[i][j] = 'o';
				else
					s[i][j] = 'x';
				br[i] = true;
				bc[j] = true;
				break;
				//printf("rc,%d %d\n",i,j);
			}
		}
		for (int i = 1; i <= n; ++i)
			for (int j = 1; j <= n; ++j) {
				if (s[i][j] != a[i][j]) {
					tail++;
					ansc[tail] = s[i][j];
					ansx[tail] = i;
					ansy[tail] = j;
				}
			}
		printf("Case #%d: %d %d\n", ++ri, ans, tail);
		for (int i = 1; i <= tail; ++i)
			printf("%c %d %d\n", ansc[i], ansx[i], ansy[i]);
	}
	return 0;
}
