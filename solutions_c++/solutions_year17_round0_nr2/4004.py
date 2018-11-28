#include <iostream>
#include <string>

using namespace std;

int main() {
	int t;
	long long n;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		string sn;
		long long ans = 0;
		cin >> n;
		while (n > 0) {
			sn = (char)(n % 10 + '0') + sn;
			n /= 10;
		}
		for (int j = sn.size() - 1; j > 0; j--) {
			if (sn[j] < sn[j - 1]) {
				for (int l = j; l < sn.size(); l++) sn[l] = '9';
				sn[j - 1]--;
			}
		}
		for (int j = 0; j < sn.size(); j++) {
			ans = (ans * 10) + sn[j] - '0';
		}
		cout << "Case #" << i << ": " << ans << endl;
	}
	return 0;
}