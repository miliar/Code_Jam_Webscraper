#include <bits/stdc++.h>
using namespace std;

int cnt[5];
int T, t_;
int n, p;
int f[101][101][101][4];

void get_max(int &a, int b) {
	if (a < b) a = b;
}

int solve(int x, int y, int z, int res) {
	if (f[x][y][z][res] != -1) return f[x][y][z][res];
	if (x)
		get_max(f[x][y][z][res], solve(x - 1, y, z, (res + 1) % p) + ((res + 1) % p == 0));
	if (y)
		get_max(f[x][y][z][res], solve(x, y - 1, z, (res + 2) % p) + ((res + 2) % p == 0));
	if (z)
		get_max(f[x][y][z][res], solve(x, y, z - 1, (res + 3) % p) + ((res + 3) % p == 0));
	return f[x][y][z][res];
}

int main() {
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	for (scanf("%d",&T); T; T--) {
		memset(f,-1,sizeof(f));
		printf("Case #%d: ",++t_);
		cnt[0] = cnt[1] = cnt[2] = cnt[3] = 0;
		scanf("%d %d",&n,&p);		
		memset(f, -1, sizeof(f));
		for (int x = 0; x < p; x++)
			f[0][0][0][x] = (x != 0);
		for (int i = 1; i <= n; i++) {
			int a;
			scanf("%d",&a); a %= p;
			cnt[a]++;
		}
		int ans = cnt[0];
		ans += solve(cnt[1], cnt[2], cnt[3], 0);
		printf("%d\n",ans);
	}
	return 0;
}
