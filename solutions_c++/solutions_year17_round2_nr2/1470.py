#include <bits/stdc++.h>

using namespace std;
const int N = 1e3 + 3;
int main() {
#ifndef ONLINE_JUDGE
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);
#endif
	int t;
	scanf("%d", &t);
	for (int test = 1; test <= t; ++test) {
		int n, r, o, y, g, b, v;
		scanf("%d %d %d %d %d %d %d", &n, &r, &o, &y, &g, &b, &v);
		pair<int, char> ch[3] = {{r, 'R'},
								 {b, 'B'},
								 {y, 'Y'}};
		sort(ch, ch + 3);
		
		string result(ch[2].first, ch[2].second);
		int i = 0;
		while (ch[1].first) {
			i %= result.size();
			result.insert(result.begin() + i, ch[1].second);
			--ch[1].first;
			i += 2;
		}
		while (ch[0].first) {
			i %= result.size();
			result.insert(result.begin() + i, ch[0].second);
			--ch[0].first;
			i += 2;
		}
		
		printf("Case #%d: ", test);
		if (result.back() != result[result.size() - 2]) {
			printf("%s\n", result.c_str());
		} else {
			printf("IMPOSSIBLE\n");
		}
	}
	return 0;
}
