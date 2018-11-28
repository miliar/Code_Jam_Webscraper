#include<bits/stdc++.h>
using namespace std;
const int N(1111);
int cnt[N], s[N];
int main() {
	int tests;
	scanf("%d", &tests);
	for(int qq(1); qq <= tests; qq++) {
		int n, m, c;
		scanf("%d%d%d", &n, &c, &m);
		fill(cnt + 1, cnt + 1 + c, 0);
		fill(s, s + 1 + n, 0);
		int ans(0);
		for(int i(1); i <= m; i++) {
			int x, y;
			scanf("%d%d", &x, &y);
			s[x]++;
			cnt[y]++;
			ans = max(ans, cnt[y]);
		}
		for(int i(1); i <= n; i++) {
			s[i] += s[i - 1];
			ans = max(ans, (s[i] + i - 1) / i);
		}
		int a1(0);
		for(int i(1); i <= n; i++) {
			a1 += max(0, (s[i] - s[i - 1]) - ans);
		}
		printf("Case #%d: %d %d\n", qq, ans, a1);
	}
}
