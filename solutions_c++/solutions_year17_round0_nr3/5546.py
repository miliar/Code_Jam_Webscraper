#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <algorithm>
using namespace std;
const int MAXN = 1000;
int a[MAXN + 2];
int ls(int s)
{
	int result = 0;
	while (a[--s] == 0)
		result++;
	return result;
}
int rs(int s)
{
	int result = 0;
	while (a[++s] == 0)
		result++;
	return result;
}
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t, i, n, k, j, l, temp, temp_ls, temp_rs, mins[MAXN + 2], maxs[MAXN + 2];
	cin >> t;
	a[0] = 1;
	for (i = 1; i <= t; i++)
	{
		cin >> n >> k;
		for (j = 1; j <= n; j++)
			a[j] = 0;
		a[n + 1] = 1;
		for (j = 0; j < k; j++)
		{
			for (l = 1; l <= n; l++)
				if (a[l] == 0)
				{
					temp_ls = ls(l);
					temp_rs = rs(l);
					mins[l] = min(temp_ls, temp_rs);
					maxs[l] = max(temp_ls, temp_rs);
				}
				else
				{
					mins[l] = -1;
					maxs[l] = -1;
				}
			temp = 1;
			for (l = 2; l <= n; l++)
				if (mins[temp] < mins[l] || mins[temp] == mins[l] && maxs[temp] < maxs[l])
					temp = l;
			a[temp] = 1;
		}
		cout << "Case #" << i << ": " << maxs[temp] << " " << mins[temp] << endl;
	}
	return 0;
}
