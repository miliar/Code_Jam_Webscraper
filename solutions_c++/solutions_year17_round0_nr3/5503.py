#include<iostream>
#include<cstring>
#include<algorithm>
#include<cmath>
using namespace std;
int main()
{
	int t, k, n;
	cin >> t;
	for (int i = 1; i <= t; ++i)
	{
		int maxnum, minnum;
		cin >> n >> k;
		int x[n + 2], xmax[n + 2], xmin[n + 2];
		memset(x, 0, sizeof(x));
		memset(xmax, -1, sizeof(xmax));
		memset(xmin, -1, sizeof(xmin));
		x[0] = x[n + 1] = 1;
		int ii;
		while (k--)
		{
			for (int i = 1; i <= n; ++i)
			{
				int counterl = 0, counterr = 0;
				for (int ii = i - 1;; --ii)
				{
					if (x[ii] == 1)
						break;
					++counterl;
				}
				for (int ii = i + 1;; ++ii)
				{
					if (x[ii] == 1)
						break;
					++counterr;
				}
				xmax[i] = max(counterl, counterr);
				xmin[i] = min(counterl, counterr);
			}
			for (int i = 1; i <= n; ++i)
			{
				if (x[i] == 0)
				{
					minnum = xmin[i];
					maxnum = xmax[i];
					ii = i;
					break;
				}
			}
			for (int i = 1; i <= n; ++i)
			{
				if (minnum < xmin[i] && x[i] == 0)
				{
					minnum = xmin[i];
					maxnum = xmax[i];
					ii = i;
				}
			}
			for (int i = 1; i <= n; ++i)
			{
				if (xmin[i] == minnum&&x[i] == 0)
				{
					if (xmax[i] > maxnum)
					{
						ii = i;
						maxnum = xmax[i];
					}
				}
			}
			x[ii] = 1;
		}
		cout << "Case #" << i << ": ";
		cout << xmax[ii] << " " << xmin[ii] << endl;
	}
}