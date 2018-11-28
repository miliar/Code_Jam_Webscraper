#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<cstdio>
#include<cmath>
#include<iomanip>
#include<vector>
#include<algorithm>

using namespace std;

const int N = 1100;

long double pi = atan(1) * 4;

struct node
{
	int r, h;
	node(int _r = 0, int _h = 0) : r(_r), h(_h) {
	}
	bool operator < (const node& b) const {
		return (double)r * h > (double)b.r * b.h;
	}
};

node a[N];

void work()
{
	int n, k;
	cin >> n >> k;
	for (int i = 1; i <= n; ++i) {
		scanf("%d%d", &a[i].r, &a[i].h);
	}
	sort(a + 1, a + n + 1);
	long double ans = 0.0;
	int maxr = 0;
	for (int i = 1; i < k; ++i) {
		ans += 2.0 * a[i].r * a[i].h;
		maxr = max(maxr, a[i].r);
	}
	long double maxbt = 0.0;
	for (int i = k; i <= n; ++i) {
		long double bt = (long double)max(maxr, a[i].r);
		long double t = bt * bt + 2.0 * a[i].r * a[i].h;
		maxbt = max(maxbt, t);
	}
	cout << fixed << setprecision(12) << (ans + maxbt) * pi << endl;
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
