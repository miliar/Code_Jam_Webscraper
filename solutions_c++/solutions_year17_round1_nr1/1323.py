#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
#define N 25 + 5

int Case, n, m;
char s[N][N];

int main()
{
	scanf("%d", &Case);
	for (int T = 1; T <= Case; T ++)
	{
		printf("Case #%d:\n", T);
		scanf("%d%d", &n, &m);
		for (int i = 0; i < n; i ++)
			scanf("%s", s[i]);
		for (int i = 0; i < n; i ++)
			for (int j = 1; j < m; j ++)
				s[i][j] = s[i][j] == '?' ? s[i][j - 1] : s[i][j];
		for (int i = 0; i < n; i ++)
			for (int j = m - 2; ~j; j --)
				s[i][j] = s[i][j] == '?' ? s[i][j + 1] : s[i][j];
		for (int j = 0; j < m; j ++)
			for (int i = 1; i < n; i ++)
				s[i][j] = s[i][j] == '?' ? s[i - 1][j] : s[i][j];
		for (int j = 0; j < m; j ++)
			for (int i = n - 2; ~i; i --)
				s[i][j] = s[i][j] == '?' ? s[i + 1][j] : s[i][j];
		for (int i = 0; i < n; i ++) printf("%s\n", s[i]);
	}
	return 0;
}
