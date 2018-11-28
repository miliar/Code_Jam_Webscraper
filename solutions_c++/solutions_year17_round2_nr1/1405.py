#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<cstdio>
#include<cmath>
#include<algorithm>
#include<string>
#include<iomanip>
#include<vector>
#include<map>
#include<set>

using namespace std;

const int N = 1100;
int k[N], s[N];

void work()
{
	int d, n;
	cin >> d >> n;
	double mt = 0;
	for (int i = 1; i <= n; ++i) {
		scanf("%d%d", &k[i], &s[i]);
		mt = max(mt, double(d - k[i]) / s[i]);
	}
	cout << fixed << setprecision(9) << d / mt << endl;
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
