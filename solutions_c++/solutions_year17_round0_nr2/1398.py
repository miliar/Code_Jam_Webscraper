#include <bits/stdc++.h>
using namespace std;
const int N = 30;
int nn[N], len, ans[N];
char s[N];
bool vis[N][2][10];
long long A;
void dfs(int x, int on, int las = 0) {
	if (x == len) {
		long long a = 0;
		for (int i = 0; i < len; ++ i) a = a * 10 + ans[i];
		A = a;
		return;
	}
	if (vis[x][on][las]) return;
	vis[x][on][las] = 1;
	for (int i = (on ? nn[x] : 9); i >= 0; -- i) {
		if (i < las) continue;
		ans[x] = i;
		dfs(x + 1, on && (i == nn[x]), i);
		if (A != -1) return;
	}
}
int main() {
	int T, zzz = 0;
	scanf("%d", &T);
	while (T --) {
		scanf("%s", s);
		len = (int) strlen(s);
		for (int i = 0; i < len; ++ i) nn[i] = s[i] - '0';
		memset(vis, 0, sizeof(vis));
		A = -1;
		dfs(0, 1);
		printf("Case #%d: %I64d\n", ++ zzz, A);
	}
}

