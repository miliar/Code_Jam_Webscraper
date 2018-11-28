#include<cstdio>
int n, c, m;
int ticket[1010][2];
int pcnt[1010];
int bcnt[1010];
int main() {
	int tcn;
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &tcn);
	for (int tc = 1; tc <= tcn; tc++) {
		scanf("%d%d%d", &n, &c, &m);
		for (int i = 0; i < m; i++) {
			scanf("%d%d", &ticket[i][0], &ticket[i][1]);
		}
		for (int i = 0; i <= n + 1; i++) {
			pcnt[i] = 0;
		}
		for (int i = 0; i <= c + 1; i++) {
			bcnt[i] = 0;
		}
		for (int i = 0; i < m; i++) {
			pcnt[ticket[i][0]]++;
			bcnt[ticket[i][1]]++;
		}
		int ans = 0;
		int bans = 0;
		for (int i = 1; i <= c; i++) {
			if (bcnt[i] > ans)ans = bcnt[i];
		}
		int s = 0;
		for (int i = 1; i <= n; i++) {
			s += pcnt[i];
			if ((s + i - 1) / i > ans)ans = (s + i - 1) / i;
		}
		for (int i = 1; i <= n; i++) {
			if (pcnt[i] > ans)bans += pcnt[i] - ans;
		}
		printf("Case #%d: %d %d\n", tc, ans, bans);
	}
	return 0;
}
