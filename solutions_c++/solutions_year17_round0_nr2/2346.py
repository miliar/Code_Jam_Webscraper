#include <bits/stdc++.h>
#define ll long long
#define rep(i,to) for(int i=0;i<(to);i++)
#define rep1(i,to) for(int i=1;i<=(to);i++)
#define ms(x, v) memset(x, v, sizeof(x))
using namespace std;
const int N = 105;
char s[N];
int n;
void dfs(int p)
{
	if (p == 0) return;
	if (s[p] < '0')
	{
		for (int i = p; i <= n; i++) s[i] = '9';
		s[p - 1]--;
		dfs(p - 1);
		return;
	}
	if (p < n)
	{
		if (s[p] > s[p + 1])
		{
			s[p]--;
			for (int i = p + 1; i <= n; i++) s[i] = '9';
			// dfs(p - 1);
		}
	}
	dfs(p - 1);
}
int main()
{
#ifdef LOCAL
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
#endif
	ios::sync_with_stdio(0);
	int T, cas = 0;
	cin >> T;
	while (T--)
	{
		cin >> (s + 1);
		n = strlen(s + 1);
		// s[n]--;
		dfs(n);
		printf("Case #%d: ", ++cas);
		int bg = 0;
		rep1(i, n)
		{
			if (s[i] != '0') bg = 1;
			if (bg) putchar(s[i]);
		}
		if (!bg) putchar('0');
		puts("");
	}
	return 0;
}