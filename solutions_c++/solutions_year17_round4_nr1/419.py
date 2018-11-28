#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

const int N = 105;
bool vis[5][N][N][N];
int f[5][N][N][N];
int n, P, T, cas;
int a[N], cnt[10];

int dfs(int r, int r1, int r2, int r3) {
	if(r1 + r2 + r3 == 0) return 0;
	int &x = f[r][r1][r2][r3];
	if(vis[r][r1][r2][r3]) return x;
	vis[r][r1][r2][r3] = true;
	x = 0;
	if(r1) {
		if(r) x = max(x, dfs(r-1, r1-1, r2, r3));
		else x = max(x, dfs(P-1, r1-1, r2, r3)+1);
	}
	if(r2) {
		if(r>=2) x = max(x, dfs(r-2, r1, r2-1, r3));
		else if(r == 1) x = max(x, dfs(r+P-2, r1, r2-1, r3));
		else x = max(x, dfs(P-2, r1, r2-1, r3)+1);
	}
	if(r3) {
		if(r>=3) x = max(x, dfs(r-3, r1, r2, r3-1));
		else if(r) x = max(x, dfs(r+P-3, r1, r2, r3-1));
		else x = max(x, dfs(P-3, r1, r2, r3-1)+1);
	}
	//printf("%d %d %d %d = %d\n", r, r1, r2, r3, x);
	return x;
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A.out", "w", stdout);
	scanf("%d", &T);
	for (cas = 1; cas <= T; cas++) {
		scanf("%d%d", &n, &P);
		memset(cnt, 0, sizeof(cnt));
		for (int i = 0; i < n; i++) scanf("%d", &a[i]);
		for (int i = 0; i < n; i++) {
			a[i] %= P;
			cnt[a[i]]++;
		}
		memset(vis, 0, sizeof(vis));

		printf("Case #%d: %d\n", cas, cnt[0]+dfs(0, cnt[1], cnt[2], cnt[3]));
	}
	return 0;
}