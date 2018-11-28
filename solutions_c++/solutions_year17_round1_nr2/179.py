#include <cstdio>
#include <iostream>
#include <string>
#include <algorithm>
#include <cmath>
using namespace std;

double a[55][55], b[55];
int p[55];
double eps = 1e-10;

int main()
{
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);
	int T;
	cin>>T;
	for (int t = 1; t <= T; t++)
	{
		int n, m, ans = 0;
		cin>>n>>m;
		for (int i = 1; i <= n; i++)
			cin>>b[i];
		for (int i = 1; i <= n; i++)
		{
			for (int j = 1; j <= m; j++)
			{
				cin>>a[i][j];
				a[i][j] /= b[i];
			}
			sort(a[i]+1, a[i]+m+1);
		}
		for (int i = 1; i <= n; i++)
			p[i] = 1;
		while (1)
		{
			double m1 = 1e9, m2 = -1e9;
			int tmp;
			for (int i = 1; i <= n; i++)
			{
				if (a[i][p[i]] < m1)
				{
					m1 = a[i][p[i]];
					tmp = i;
				}
				if (a[i][p[i]] > m2)
					m2 = a[i][p[i]];
			}
			int t2 = (int)ceil(m2/1.1-eps);
			int t1 = (int)floor(m1/0.9+eps);
			if (t1 >= t2)
			{
				ans++;
				for (int i = 1; i <= n; i++)
					p[i]++;
			}
			else
				p[tmp]++;
			for (int i = 1; i <= n; i++)
				if (p[i] > m)
					goto out;
		}
		out:
		cout<<"Case #"<<t<<": "<<ans<<endl;
	}
	return 0;
}