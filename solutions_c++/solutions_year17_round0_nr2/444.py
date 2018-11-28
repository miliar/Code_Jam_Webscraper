#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

int main() {
	ios::sync_with_stdio(false);
	int T;
	cin >> T;
	for (int tc = 1; tc <= T; ++tc) {
		cout << "Case #" << tc << ": ";
		string x;
		cin >> x;
		for (int i = 0; i+1 < x.size(); ++i) {
			if (x[i] > x[i+1]) {
				--x[i];
				for (int j = i+1; j < x.size(); ++j) x[j] = '9';
			}
		}
		for (int i = x.size()-1; i-1 >= 0; --i) {
			if (x[i-1] > x[i]) {
				x[i] = '9';
				x[i-1]--;
			}
		}
		int i = 0;
		while (i < x.size() && x[i] == '0') ++i;
		for (; i < x.size(); ++i) cout << x[i];
		cout << '\n';
	}
}