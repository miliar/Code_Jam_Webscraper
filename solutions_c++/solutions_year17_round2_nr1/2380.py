#include <fstream>

using namespace std;

ifstream cin("input.txt");
ofstream cout("output.txt");

typedef long double ld;

ld solve() {
	int n;
	ld d, k, s, t = 0;
	cin >> d >> n;
	for (int i = 0; i < n; ++i) {
		cin >> k >> s;
		t = max(t, (d - k) / s);
	}
	return d / t;
}

int main() {
	ios_base::sync_with_stdio(0);
	cout.precision(10);
	cout << fixed;
	int t;
	cin >> t;
	for (int i = 1; i <= t; ++i)
		cout << "Case #" << i << ": " << solve() << endl;
	cin >> t;
	return 0;
}