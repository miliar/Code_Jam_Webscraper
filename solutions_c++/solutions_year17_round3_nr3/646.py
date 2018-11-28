#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<cstdio>
#include<cmath>
#include<iomanip>
#include<vector>
#include<algorithm>

using namespace std;

const int N = 100;
const double EPS = 1e-10;

double a[N];

void work()
{
	int n, k;
	cin >> n >> k;
	double u;
	cin >> u;
	for (int i = 1; i <= n; ++i) {
		cin >> a[i];
	}
	a[n + 1] = 100.0;
	sort(a + 1, a + n + 1);
	for (int i = 1; i <= n; ++i) {
		double maxt = (a[i + 1] - a[i]) * i;
		if (maxt >= u) {
			for (int j = 1; j <= i; ++j) {
				a[j] += u / i;
			}
			break;
		}
		else {
			for (int j = 1; j <= i; ++j) {
				a[j] += maxt / i;
			}
			u -= maxt;
		}
	}
	double ans = 1.0;
	for (int i = 1; i <= n; ++i) {
		ans *= a[i];
	}
	cout << fixed << setprecision(12) << ans << endl;
}

int main()
{
	freopen("my.in", "r", stdin);
	freopen("out.txt", "w", stdout);

	int q;
	cin >> q;
	for (int i = 1; i <= q; ++i) {
		printf("Case #%d: ", i);
		work();
	}
	return 0;
}
