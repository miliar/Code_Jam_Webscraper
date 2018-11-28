#include <cstdio>
#include <cstring>
using namespace std;
const int N = 1005;

int n, k;
char s[N];

inline char opp(char c) { return c == '+' ? '-' : '+'; }

int solve()
{
	int cnt = 0;
	for (int i = 1; i <= n - k; ++i)
		if (s[i] == '-')
		{
			++cnt;
			for (int j = i; j < i + k; ++j)
				s[j] = opp(s[j]);
		}
	for (int i = n - k + 1; i <= n; ++i)
		if (s[i] != s[n]) return -1;
	if (s[n] == '-') ++cnt;
	return cnt;
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int cas = 1; cas <= T; ++cas)
	{
		scanf("%s%d", s + 1, &k);
		n = strlen(s + 1);
		printf("Case #%d: ", cas);
		int t = solve();
		if (t == -1) puts("IMPOSSIBLE");
		else printf("%d\n", t);
	}
	return 0;
}
