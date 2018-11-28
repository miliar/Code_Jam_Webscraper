#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <algorithm>
using namespace std;

void solve()
{
	int m, n;
	scanf("%d %d", &m, &n);
	double ans = 1e100;
	for (int i = 0; i < n; ++i)
	{
		int k, s;
		scanf("%d %d", &k, &s);
		double tmp = ((double)k / (m-k) + 1) * s;
		if (ans > tmp)
			ans = tmp;
	}
	printf("%.6lf\n", ans);
}

int main()
{
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int times;
	scanf("%d", &times);
	for (int i = 1; i <= times; ++i)
	{
		printf("Case #%d: ", i);
		solve();
	}
	return 0;
}