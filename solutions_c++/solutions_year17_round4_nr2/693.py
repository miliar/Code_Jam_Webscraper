#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <cstdlib>
#include <ctime>
#include <map>
#include <set>
#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;

const int maxn = 1010;
int rsum[maxn], csum[maxn], cmax;

void solve()
{
	int ans = 0;
	int n, m, p;
	memset(rsum,0,sizeof(rsum));
	memset(csum,0,sizeof(csum));
	cmax = 0;
	cin >> n >> m >> p;
	for (int i = 0; i < p; ++i)
	{
		int r, c;
		cin >> r >> c;
		--r;
		--c;
		++rsum[r];
		++csum[c];
		if (cmax < csum[c])
			cmax = csum[c];
	}
	int num = 0;
	while (1)
	{
		int rmax = 0;
		for (int i = 0; i < n; ++i)
			if (rsum[rmax] < rsum[i])
				rmax = i;
		if (rsum[rmax] <= cmax)
		{
			cout << cmax << " " << num << endl;
			return;
		}
		if (rmax == 0)
		{
			cout << rsum[rmax] << " " << num << endl;
			return;
		}
		int rmin = 0;
		for (int i = 0; i < rmax; ++i)
			if (rsum[rmin] > rsum[i])
				rmin = i;
		if (rsum[rmax] - rsum[rmin] <= 1)
		{
			cout << rsum[rmax] << " " << num << endl;
			return;
		}
		--rsum[rmax];
		++rsum[rmin];
		++num;
	}
}

int main()
{
	int times;
	freopen("a.in","r",stdin);
	freopen("a.txt","w",stdout);
	scanf("%d", &times);
	for (int i = 1; i <= times; ++i)
	{
		printf("Case #%d: ", i);
		solve();
	}
	return 0;
}