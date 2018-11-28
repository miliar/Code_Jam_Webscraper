#include <bits\stdc++.h>

using namespace std;

typedef long long ll;
#define N int(1e3+5)

int main() {
	ifstream cin("A-large.in");
	ofstream cout("output.txt");
	int t, k, n, ans, cc;
	string s;
	cin >> t;
	for (int test = 1; test <= t; test++) {
		ans = 0;
		cin >> s >> k;
		n = s.length();
		vector<int> c(n);
		cc = 0;
		bool f = false;
		for (int i = 0; i < n - k + 1; i++) {
			if (((s[i] == '-') + cc) % 2) {
				ans++;
				cc++;
				c[i + k - 1]--;
			}
			cc += c[i];
		}
		for (int i = n - k + 1; i < n; i++) {
			if (((s[i] == '-') + cc) % 2) {
				f = true;
			}
			cc += c[i];
		}
		cout << "Case #" << test << ": ";
		if (f)
			cout << "IMPOSSIBLE\n";
		else
			cout << ans << endl;
	}
}