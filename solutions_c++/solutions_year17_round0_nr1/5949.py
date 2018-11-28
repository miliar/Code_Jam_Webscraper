#include <cstdio>
#include <cstdlib>
#include <queue>
#include <cstring>

const int MAXN = 1007;

std::queue<int> que;

char s[MAXN];

int main() {
	int Cases;
	scanf("%d", &Cases);
	for (int Case = 1; Case <= Cases; ++Case) {
		scanf("%s", s);
		int k;
		scanf("%d", &k);
		while (!que.empty()) que.pop();
		int n = strlen(s);
		bool flag = 0;
		int cnt = 0;
		for (int i = 0; i < n; ++i) {
			if (!que.empty() && que.front() + k == i) que.pop();
			int u = (s[i] == '-') + (int)que.size();
			if ((u & 1)) {
				if (i + k > n) flag = 1;
				que.push(i);
				++cnt;
			}
		}
		printf("Case #%d: ", Case);
		if (flag) printf("IMPOSSIBLE\n");
		else printf("%d\n", cnt);
	}
	return 0;
}
