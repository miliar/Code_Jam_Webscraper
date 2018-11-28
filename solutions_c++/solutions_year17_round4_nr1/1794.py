#include <bits/stdc++.h>

using namespace std;

int n, p, a[110];

int countR(int r) {
	int cnt = 0;
	for(int i=0; i<n; i++)
		cnt += (int)(a[i] % p == r);
	return cnt;
}

int cal2() {
	int c1 = countR(1);
	return n - c1 / 2;
}

int cal3() {
	int c1 = countR(1), c2 = countR(2);
	int res = min(c1, c2);
	c1 -= res;
	c2 -= res;
	res += (c1 / 3 * 2 + (int)(c1 % 3 == 2));
	res += (c2 / 3 * 2 + (int)(c2 % 3 == 2));
	return n - res;
}

int main() {
	int _T;
	cin >> _T;
	for(int _t = 1; _t <= _T; _t++) {
		cout << "Case #" << _t << ": ";
		int res;
		cin >> n >> p;
		for(int i=0; i<n; i++)
			cin >> a[i];
		if (p == 1)
			res = n;
		else if (p == 2)
			res = cal2();
		else if (p == 3)
			res = cal3();
		cout << res << "\n";
	}
	return 0;
}