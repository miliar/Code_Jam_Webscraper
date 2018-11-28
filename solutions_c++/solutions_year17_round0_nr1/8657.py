#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

const int N = 11;
char s[N + 1];
bool vis[1 << N];
queue<int> qu;
int n, k;

int BFS(int src, int dest) {
	if (src == dest)
		return 0;
	memset(vis, false, sizeof vis);
	while (!qu.empty())
		qu.pop();
	qu.push(src);
	int cost = 1;
	while (!qu.empty()) {
		int size = qu.size();
		while (size-- != 0) {
			int mask = qu.front();
			qu.pop();
			for (int i = 0; i + k <= n; ++i) {
				bitset<N> bs = mask;
				for (int j = 0; j < k; ++j)
					bs[i + j].flip();
				int nmask = bs.to_ulong();
				if (nmask == dest)
					return cost;
				if (!vis[nmask]) {
					vis[nmask] = true;
					qu.push(nmask);
				}
			}
		}
		++cost;
	}
	return -1;
}

int main() {
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t, cas = 1;
	scanf("%d", &t);
	while (t-- != 0) {
		printf("Case #%d: ", cas++);
		scanf("%s%d", s, &k);
		n = strlen(s);
		int src = 0;
		for (int i = n - 1; i >= 0; --i)
			if (s[i] == '+')
				src += 1 << (n - i - 1);
		int res = BFS(src, (1 << n) - 1);
		if (res == -1)
			puts("IMPOSSIBLE");
		else
			printf("%d\n", res);
	}
	return 0;
}
