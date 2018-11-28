#include <bits/stdc++.h>

using namespace std;

const int MAXN = (int)2e5 + 256;

typedef long long ll;

char s[5000];
int d[2000];

int main() {
	int t, Case = 0; scanf("%d", &t);
	while (t--) {
		int k;
		scanf("%s%d", s, &k);

		int n = strlen(s);
		int cur = 0;
		
		for (int i = 0; i < n; ++i) {
			if (s[i] == '+')
				cur += (1 << i);
		}
		queue <int> q;
		memset(d, -1, sizeof d);
		d[cur] = 0;
		q.push(cur);
		while (!q.empty()) {
			int v = q.front();
			q.pop();
			for (int i = 0; i + k <= n; ++i) {
				int nxt = v;
				for (int j = i; j < i + k; ++j) {
					nxt ^= (1 << j);
				}
				if (-1 == d[nxt]) {
					d[nxt] = d[v] + 1;
					q.push(nxt);
				}
			}
		}
		printf("Case #%d: ", ++Case);
		if (~d[(1 << n) - 1]) {
			printf("%d\n", d[(1 << n) - 1]);
		} else {
			puts("IMPOSSIBLE");
		}
	}
	return 0;
}

