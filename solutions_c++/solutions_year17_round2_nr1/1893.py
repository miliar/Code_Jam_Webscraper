#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <iomaniP>
#include <algorithm>
using namespace std;
const int MAXN = 2000;
struct ks
{
	int k0;
	double k;
	int s;
} a[MAXN];
bool compare(ks ks1, ks ks2)
{
	return ks1.k <= ks2.k;
}
double min(int m, double n)
{
	if (m <= n)
		return m;
	return n;
}
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t, i, d, n, j;
	double te;
	cin >> t;
	for (i = 1; i <= t; i++)
	{
		cin >> d >> n;
		for (j = 0; j < n; j++)
		{
			cin >> a[j].k0 >> a[j].s;
			a[j].k = (double) a[j].k0;
		}
		sort(a, a + n, compare);
		te = 0;
		for (j = n - 1; j >= 0; j--)
		{
			a[j].k = min(d, a[j].k + a[j].s * te);
			te += (d - a[j].k) / (double)a[j].s;
		}
		cout << fixed;
		cout << setprecision(7);
		cout << "Case #" << i << ": " << d / te << endl;
	}
	return 0;
}
