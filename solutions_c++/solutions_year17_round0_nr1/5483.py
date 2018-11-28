#include <cstdio>
#include <cmath>
#include <map>
#include <queue>
using namespace std;
int main() {
	int T; scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		char str[11] = {};
		int K, len, val = 0;
		scanf("%s%d", str, &K);
		for (len = 0; str[len]; len++) {
			val <<= 1;
			val |= str[len] == '+' ? 1 : 0;
		}
		map<int, int> m; queue<int> q;
		m[val] = 0; q.push(val);
		int ans = (1 << len) - 1;
		while (!q.empty() && m.find(ans) == m.end()) {
			int x = q.front(); q.pop();
			for (int i = 0; i < len - K + 1; i++) {
				int xx = x ^ (((1 << K) - 1) << i);
				if (m.find(xx) == m.end()) {
					m[xx] = m[x] + 1;
					q.push(xx);
				}
			}
		}
		if (m.find(ans) == m.end()) printf("Case #%d: IMPOSSIBLE\n", t);
		else printf("Case #%d: %d\n", t, m[ans]);
	}
	return 0;
}