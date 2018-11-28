#include<cstdio>
#include<cstdlib>
#include<iostream>
#include<algorithm>
using namespace std;

const int N = 2882 * 2;
const int MAXT = 1440 * 2;

int na,nb;
int a[N], b[N];
int f[N][2];
int tmp[N][2];

int main(int argc, char *argv[])
{
	if (argc == 1)
	{
		freopen("in","r",stdin);
		freopen("out","w",stdout);
	}
	else
	{
		freopen(argv[1], "r", stdin);
		freopen("ans", "w",stdout);
	}

	int T;
	cin >> T;
	for (int Case = 1;Case <= T;++ Case)
	{
		scanf("%d%d", &na, &nb);
		for (int i = 0;i < MAXT;++ i)
		{
			a[i] = b[i] = 0;
			f[i][0] = f[i][1] = 3000;
		}
		for (int i = 0;i < na;++ i)
		{
			int s, t;
			scanf("%d%d", &s, &t);
			for (int j = s;j < t;++ j)
				a[j] = a[j+1440] = 1;
		}
		for (int i = 0;i < nb;++ i)
		{
			int s, t;
			scanf("%d%d", &s, &t);
			for (int j = s;j < t;++ j)
				b[j] = b[j+1440] = 1;
		}
		int ans = 100000;
		if (a[0] == 0)
		{
			f[1][0] = 0;
			for (int i = 1;i < 1440;++ i)
			{
				for (int j = 0;j <= 720;++ j)
				{
					tmp[j][0] = f[j][0];
					tmp[j][1] = f[j][1];
					f[j][0] = f[j][1] = 3000;
				}
				for (int j = max(0, i-719);j <= min(i+1, 720);++ j)
				{
					if (a[i] == 0)
					{
						if (j > 0)
							f[j][0] = min(tmp[j-1][0], tmp[j-1][1] + 1);
					}
					if (b[i] == 0)
						f[j][1] = min(tmp[j][0] + 1, tmp[j][1]);
				}
			}
			ans = min(f[720][0], f[720][1] + 1);
		}
		if (b[0] == 0)
		{
			f[0][1] = 0;
			for (int i = 1;i < 1440;++ i)
			{
				for (int j = 0;j <= 720;++ j)
				{
					tmp[j][0] = f[j][0];
					tmp[j][1] = f[j][1];
					f[j][0] = f[j][1] = 3000;
				}
				for (int j = max(0, i-719);j <= min(i+1, 720);++ j)
				{
					if (a[i] == 0)
					{
						if (j > 0)
							f[j][0] = min(tmp[j-1][0], tmp[j-1][1] + 1);
					}
					if (b[i] == 0)
						f[j][1] = min(tmp[j][0] + 1, tmp[j][1]);
				}
			}
			ans = min(ans, min(f[720][0]+1, f[720][1] ));
		}
		for (int i = 0;i < MAXT;++ i)
			f[i][0] = f[i][1] = 3000;
		printf("Case #%d: ", Case);
		printf("%d\n", ans);
	}
	return 0;
}
