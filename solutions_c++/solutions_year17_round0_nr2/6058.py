#include <bits/stdc++.h>
using namespace std;

typedef long long LL;
int testcase;
LL n;

LL solve(LL n) {
	LL N = n;
	int a[111];
	int cnt = 0;
	while (n) {
		a[++cnt] = n % 10;
		n /= 10;
	}
	for (int i = cnt; i > 1; --i) {
		if (a[i] > a[i - 1]) {
			N = 0;
			for (int j = cnt; j >= i; --j) {
				N = N * 10 + a[j];
			}
			N--;
			N = solve(N);
			for (int j = i - 1; j; --j) {
				N = N * 10 + 9;
			}
			break;
		}
	}
	return N;
}

int main() {
	cin >> testcase;
	for (int cs = 1; cs <= testcase; ++cs) {
		cin >> n;
		cout << "Case #" << cs << ": " << solve(n) << endl;
	}
}
