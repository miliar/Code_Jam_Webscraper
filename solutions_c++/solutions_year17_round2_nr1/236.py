#include <cstdio>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

int k[100500], s[100500], ind[100500];
double t[100500];

bool cmp(int i, int j)
{
	return k[i] > k[j];
}

void solve()
{
	int n, d;
	scanf("%d%d", &d, &n);
	for (int i = 0; i < n; ++i)
	{
		scanf("%d%d", &k[i], &s[i]);
		ind[i] = i;
	}
	sort(ind, ind + n, cmp);
	for (int i = 0; i < n; ++i)
	{
		t[ind[i]] = ((double)(d - k[ind[i]]))/s[ind[i]];
		if (i > 0)
		{
			t[ind[i]] = max(t[ind[i]], t[ind[i - 1]]);
		}
	}
	printf("%.8lf", ((double)d)/t[ind[n - 1]]);
}

int main()
{
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
	int tt;
	cin >> tt;
	for (int i = 0; i < tt; ++i)
	{
		cout << "Case #" << i + 1 << ": ";
		solve();
		cout << endl;
	}
	return 0;
}
