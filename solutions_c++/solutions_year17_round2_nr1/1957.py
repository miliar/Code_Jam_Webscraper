#include <iostream>
#include <iomanip>
#include <algorithm>
#include <string>
using namespace std;

double go() {
	double res = 1e14;
	int d, n, k, s;
	cin >> d >> n;
	for (int i = 0; i < n; ++i) {
		cin >> k >> s;
		res = min(res, d / (1.0 * (d - k) / s));
	}
	return res;
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("output21L.txt","w", stdout);
    
	int T; cin >> T;
	for (int c = 1; c <= T; ++c) {
		cout << "Case #" << c << ": "
			<< fixed << setprecision(6) << go() << endl;
	}
}