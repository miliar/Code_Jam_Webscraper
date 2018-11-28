#include <bits/stdc++.h>
using namespace std;
vector <long long> tidy;
void generateTidy(int digits, int previous_digit, long long x) {
	if (!digits) {
		tidy.push_back(x);
		return;
	}
	digits--;
	x *= 10;
	for (int i = 1; i < 10; ++i) {
		if (i >= previous_digit) {
			generateTidy(digits, i, x + i);
		}
	}
}
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	for (int i = 1; i <= 18; ++i) {
		generateTidy(i, 1, 0);
	}
	int T;
	cin >> T;
	for (int t = 0; t < T; ++t) {
		long long x, ans;
		cin >> x;
		for (int i = tidy.size() - 1; i >= 0; --i) {
			if (tidy[i] <= x) {
				ans = tidy[i];
				break;
			}
		}
		cout << "Case #" << t + 1 << ": " << ans << endl;
	}
	return 0;
}
