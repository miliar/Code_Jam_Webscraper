#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

int s[1005], S[1005];

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int cas = 1; cas <= T; cas++) {
		int n, C, m;
		scanf("%d%d%d", &C, &n, &m);
		//if (cas == 77) cout << n << C << m << endl;
		memset(s, 0, sizeof(s));
		memset(S, 0, sizeof(S));
		for (int i = 1; i <= m; ++i) {
			int x, y;
			scanf("%d%d", &x, &y);
			++s[y];
			++S[x];
		}
		int mm = 0;
		for (int i = 1; i <= n; ++i) {
			mm = max(mm, s[i]);
		}
		int x = mm, y = m;
		while (x <= y) {
			int z = (x + y) / 2;
			int sum = 0;
			bool flag = true;
			for (int i = 1; i <= C; ++i) {
				sum += S[i];
				if (sum > i * z) {
					flag = false;
					break;
				}
			}
			if (!flag) x = z + 1;
			else y = z - 1;
		}
		int ans = 0;
		for (int i = 1; i <= C; ++i) {
			ans += max(0, S[i] - x);
		}
		printf("Case #%d: %d %d\n", cas, x, ans);
	}
	return 0;
} 
