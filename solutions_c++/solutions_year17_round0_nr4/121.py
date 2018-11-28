#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef double db;
typedef pair<int,int> pii;
#define eprintf(...) fprintf(stderr,__VA_ARGS__)

const int N = 105, M = N * N;

int n, m;

char s[N][N];
int matx[N], maty[N], matdx[N*2], matdy[N*2];
bool con[N*2][N*2];
bool vis[N*2];

int nn, *mx, *my;

bool extend(int u) {
	for (int v = 1; v <= nn; v++) if (con[u][v] && !vis[v]) {
		vis[v] = true;
		if (my[v] == 0 || (my[v] != -1 && extend(my[v]))) {
			my[v] = u;
			mx[u] = v;
			return true;
		}
	}
	return false;
}

int hungary() {
	for (int i = 1; i <= nn; i++) vis[i] = false;
	int ans = 0;
	for (int i = 1; i <= nn; i++) if (! mx[i]) {
		for (int j = 1; j <= nn; j++) vis[j] = false;
		if (extend(i))
			ans++;
	}
	return ans;
}

int main(){
	freopen("D-large.in", "r", stdin);
	freopen("D.out", "w", stdout);
	int T; scanf("%d", &T);
	for(int Case = 1; Case <= T; Case++){
		scanf("%d%d", &n, &m);
		for(int x = 1; x <= n; x++)
			for(int y = 1; y <= n; y++)
				s[x][y] = '.';
		for(int i = 1; i <= n; i++) matx[i] = maty[i] = 0;
		for(int i = 1; i <= n * 2 - 1; i++) matdx[i] = matdy[i] = 0;
		for(int i = 0; i < m; i++) {
			char c; int x, y; scanf("\n%c%d%d", &c, &x, &y);
			s[x][y] = c;
			int dx = y - x + n, dy = x + y - 1;
			if (c == 'x' || c == 'o') {
				matx[x] = y;
				maty[y] = -1;
			}
			if (c == '+' || c == 'o') {
				matdx[dx] = dy;
				matdy[dy] = -1;
			}
		}
		int ans = 0;
		for(int i = 1; i <= n; i++)
			for(int j = 1; j <= n; j++)
				con[i][j] = true;
		nn = n;
		mx = matx;
		my = maty;
		hungary();
		for (int x = 1; x <= n; x++) if(matx[x])
			ans++;
		for(int i = 1; i <= n * 2 - 1; i++)
			for(int j = 1; j <= n * 2 - 1; j++)
				con[i][j] = false;
		for(int x = 1; x <= n; x++)
			for(int y = 1; y <= n; y++)
				con[y - x + n][x + y - 1] = true;
		nn = n * 2 - 1;
		mx = matdx;
		my = matdy;
		hungary();
		for (int dx = 1; dx <= n * 2 - 1; dx++) if(matdx[dx])
			ans++;
		int m_ = 0;
		for(int x = 1; x <= n; x++)
			for(int y = 1; y <= n; y++){
				int dx = y - x + n, dy = x + y - 1;
				bool flag = matx[x] == y;
				bool flagd = matdx[dx] == dy;
				char c;
				if (flag) {
					if (flagd) {
						c = 'o';
					}
					else {
						c = 'x';
					}
				}
				else {
					if (flagd) {
						c = '+';
					}
					else {
						c = '.';
					}
				}
				if (c != s[x][y])
					m_++;
			}
		printf("Case #%d: %d %d\n", Case, ans, m_);
		for(int x = 1; x <= n; x++)
			for(int y = 1; y <= n; y++){
				int dx = y - x + n, dy = x + y - 1;
				bool flag = matx[x] == y;
				bool flagd = matdx[dx] == dy;
				char c;
				if (flag) {
					if (flagd) {
						c = 'o';
					}
					else {
						c = 'x';
					}
				}
				else {
					if (flagd) {
						c = '+';
					}
					else {
						c = '.';
					}
				}
				if (c != s[x][y]) {
					printf("%c %d %d\n", c, x, y);
				}
			}
	}
}
