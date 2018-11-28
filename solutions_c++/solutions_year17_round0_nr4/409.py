#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <map>
using namespace std;

const int maxn = 110;
int a0[maxn][maxn], a1[maxn][maxn];
int b0[maxn][maxn], b1[maxn][maxn];

void solve()
{
	map<int, int> oar, oac, obl, obr;
	memset(a0, 0, sizeof(a0));
	memset(a1, 0, sizeof(a1));
	memset(b0, 0, sizeof(b0));
	memset(b1, 0, sizeof(b1));
	int n, k;
	cin >> n >> k;
	int ans = 0;
	while (k--)
	{
		char ch;
		int x, y;
		cin >> ch >> x >> y;
		if (ch == '+' || ch == 'o')
		{
			++ans;
			b0[x][y] = b1[x][y] = 1;
			obl[x+y] = 1;
			obr[x-y] = 1;
		}
		if (ch == 'x' || ch == 'o')
		{
			++ans;
			a0[x][y] = a1[x][y] = 1;
			oar[x] = 1;
			oac[y] = 1;
		}
	}
	int num = 0;
	for (int i = 1; i <= n; ++i)
		for (int j = 1; j <= n; ++j)
		{
			int inc = 0;
			if (oar[i] == 0 && oac[j] == 0)
			{
				a1[i][j] = 1;
				oar[i] = 1;
				oac[j] = 1;
				++ans;
				inc = 1;
			}
			if ((i==1||i==n||j==1||j==n)&&obl[i+j] == 0 && obr[i-j] == 0)
			{
				b1[i][j] = 1;
				obl[i+j] = 1;
				obr[i-j] = 1;
				++ans;
				inc = 1;
			}
			num += inc;
		}
	cout << ans << " " << num << endl;
	for (int i = 1; i <= n; ++i)
		for (int j = 1; j <= n; ++j)
		{
			int code = 0;
			if (a1[i][j] == 1 && a0[i][j] == 0)
				code |= 1;
			if (b1[i][j] == 1 && b0[i][j] == 0)
				code |= 2;
			if (a1[i][j]+b1[i][j]>a0[i][j]+b0[i][j] && a1[i][j]+b1[i][j]==2)
				code = 3;
			switch (code)
			{
				case 0:break;
				case 1:cout << "x " << i << " " << j << endl;break;
				case 2:cout << "+ " << i << " " << j << endl;break;
				case 3:cout << "o " << i << " " << j << endl;break;
			}
		}
}

int main()
{
	freopen("b.in", "r", stdin);
	freopen("b.txt", "w", stdout);
	int times;
	scanf("%d", &times);
	for (int i = 1; i <= times; ++i)
	{
		printf("Case #%d: ", i);
		solve();
	}
	return 0;
}