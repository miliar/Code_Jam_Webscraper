#define _CRT_SECURE_NO_WARNINGS
#include<cstdio>
#include<iostream>
#include<algorithm>
using namespace std;
const int MAX_N = 1005;

struct elem
{
	int k, s;
	elem() {}
	elem(int k, int s):k(k), s(s) {}
};

elem a[MAX_N];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for (int q = 0; q < t; q++)
	{
		int D, n;
		cin >> D >> n;
		for (int i = 0; i < n; i++)
			cin >> a[i].k >> a[i].s;

		double ans = 0.0;
		for (int i = 0; i < n; i++)
			ans = max(ans, (double)(D - a[i].k) / (double)a[i].s);
		ans = (double)D / ans;
		printf("Case #%d: %.7lf\n", (q + 1), ans);
	}
	return 0;
}