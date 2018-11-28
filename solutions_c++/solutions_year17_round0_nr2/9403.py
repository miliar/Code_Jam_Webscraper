#include <bits/stdc++.h>
using namespace std;
int main() {
	vector<int> a;
	for (int i = 1; i <= 1000; ++i) {
		string s = to_string(i);
		if (is_sorted(s.begin(), s.end())) a.push_back(i);
	}
	int t, cs;
	long long n, e, l;
	cin >> t;
	for (cs = 1; cs <= t; ++cs) {
		cin >> n;
		for (e = 1; e * 10 <= n; e *= 10);
		for (e /= 10; e; e /= 10)
			if (n / e % 10 < n / e % 100 / 10) {
				n -= (n / e % 10 + 1) * e;
				for (l = e * 10; l * 10 <= n; l *= 10)
					if (n / l % 10 < n / l % 100 / 10) {
						n -= l * 10;
						n += (9 - n / l % 10) * l;
					}
				for (e /= 10; e; e /= 10) n += (9 - n / e % 10) * e;
				break;
			}
		cout << "Case #" << cs << ": " << n << endl;
	}
	return 0;
}
