#include<vector>
#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
using namespace std;

const int N = 1005;

int n, c, m;

int cnta[N], cntb[N];

int main() {
	int T;
	scanf("%d", &T);
	while (T--) {
		memset(cnta, 0, sizeof(cnta));
		memset(cntb, 0, sizeof(cntb));
		scanf("%d%d%d", &n, &c, &m);
		for (int i = 0; i < m; ++i) {
			int a, b;
			scanf("%d%d", &a, &b);
			--a, --b;
			++cnta[a];
			++cntb[b];
		}
		int ans = 0;
		for (int i = 0; i < c; ++i) {
			ans = max(ans, cntb[i]);
		}
		for (int i = 0, sum = 0; i < n; ++i) {
			sum += cnta[i];
			ans = max(ans, (sum + i) / (i + 1));
		}
		int ansb = 0;
		for (int i = 0; i < n; ++i) {
			ansb += max(cnta[i] - ans, 0);
		}
		static int id = 0;
		printf("Case #%d: %d %d\n", ++id, ans, ansb);
	}
	return 0;
}
