#include<cstdio>
#define N 30

int T, n, m, fl[N];
char s[N][N];

void Init(int x)
{
	int y = 0, ny = 0;
	while (y < m)
	{
		while (s[x][y] == '?' && y < m) y++;
		if (y >= m) break;
		for (int i = ny; i < y; i++) s[x][i] = s[x][y];
		y++;
		ny = y;
	}
	y = m - 1;
	while (s[x][y] == '?') y--;
	for (int i = y + 1; i < m; i++) s[x][i] = s[x][y];
}

void Copy(int a, int b)
{
	for (int i = 0; i < m; i++) s[a][i] = s[b][i];
}

void Do()
{
	for (int i = 1; i <= n; i++) fl[i] = 0;
	for (int i = 1; i <= n; i++)
		for (int j = 0; j < m; j++) if (s[i][j] != '?') fl[i] = 1;
	for (int i = 1; i <= n; i++) if (fl[i]) Init(i);
	int x = 1, nx = 1;
	while (x <= n)
	{
		while (!fl[x] && x <= n) x++;
		if (x > n) break;
		for (int i = nx; i < x; i++) Copy(i, x);
		x++;
		nx = x;
	}
	x = n;
	while (!fl[x]) x--;
	for (int i = x + 1; i <= n; i++) Copy(i, x);
}

int main()
{
//	freopen("A.in", "r", stdin);
//	freopen("A.out", "w", stdout);
	scanf("%d", &T);
	for (int I = 1; I <= T; I++)
	{
		scanf("%d%d", &n, &m);
		for (int i = 1; i <= n; i++) scanf("%s", s[i]);
		Do();
		printf("Case #%d:\n", I);
		for (int i = 1; i <= n; i++) printf("%s\n", s[i]);
	}
	return 0;
}
