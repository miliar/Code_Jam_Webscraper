#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<cstdio>
#include<cmath>
#include<iomanip>
#include<vector>
#include<algorithm>

using namespace std;

void work()
{
	int n, m;
	cin >> n >> m;
	int a[5], b[5];
	for (int i = 1; i <= n + m; ++i) {
		cin >> a[i] >> b[i];
	}
	if (n == 1 || m == 1) {
		cout << 2 << endl;
		return;
	}
	int ans = -1;
	if (a[2] > b[1]) {
		if (a[2] - b[1] >= 720 || a[1] + 720 - b[2] >= 0) {
			ans = 2;
		}
		else {
			ans = 4;
		}
	}
	else {
		if (a[1] - b[2] >= 720 || a[2] + 720 - b[1] >= 0) {
			ans = 2;
		}
		else {
			ans = 4;
		}
	}
	cout << ans << endl;
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
