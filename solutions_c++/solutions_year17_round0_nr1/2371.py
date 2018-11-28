#include <bits/stdc++.h>
#define ll long long
#define rep(i,to) for(int i=0;i<(to);i++)
#define rep1(i,to) for(int i=1;i<=(to);i++)
#define ms(x, v) memset(x, v, sizeof(x))
using namespace std;
const int N = 1005;
char s[N];
int main()
{
#ifdef LOCAL
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
#endif
	ios::sync_with_stdio(0);
	int T, k, cas = 0;
	cin >> T;
	while (T--)
	{
		cin >> (s + 1) >> k;
		int n = strlen(s + 1), ans = 0;
		for (int i = 1; i <= n - k + 1; i++)
		{
			if (s[i] == '-')
			{
				for (int j = 0; j < k; j++)
				{
					s[i + j] = (s[i + j] == '+' ? '-' : '+');
				}
				ans++;
			}
		}
		int f = 0;
		for (int j = 0; j < k; j++)
		{
			if (s[n - j] == '-') f = 1;
		}
		if (f) printf("Case #%d: IMPOSSIBLE\n", ++cas);
		else printf("Case #%d: %d\n", ++cas, ans);
	}
	return 0;
}