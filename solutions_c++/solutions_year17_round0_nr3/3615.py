#include <bits/stdc++.h>
using namespace::std;

pair <long long, long long> f(long long n, long long k) {
	if (k == 1) {
		if (n % 2 == 0)
			return make_pair(n / 2 - 1, n / 2);
		else
			return make_pair(n / 2, n / 2);
	}
	k--;

	if (n % 2 == 1)
		return f(n / 2, ceil((k * 1.0) / 2));
	else {
		if (k % 2 == 0)
			return f(n / 2 - 1, k / 2);
		else
			return f(n / 2, ceil((k * 1.0) / 2));
	}
}

int main() {
	int t, caseno = 0;
	cin >> t;
	while (t--) {
		caseno++;
		long long n, k;
		cin >> n >> k;
		pair <long long, long long> ans = f(n, k);
		cout << "Case #" << caseno << ": " << ans.second << " " << ans.first << endl;
	}
	return 0;
}