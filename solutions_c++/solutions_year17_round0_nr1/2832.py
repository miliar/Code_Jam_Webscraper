#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
using namespace std;

int main() {
	ifstream cin("A-large.in");
	ofstream cout("output.txt");

	int T, n, k, i, j, ans;
	string s;
	cin >> T;

	for (k = 1; k <= T; ++k) {
		cin >> s >> n;
		ans = 0;

		for (i = 0; i < s.size(); ++i) {
			if (s[i] == '+')
				continue;

			if (i + n > s.size()) {
				ans = -1e9;
				break;
			}

			++ans;

			for (j = i; j < i + n; ++j)
				s[j] = (s[j] == '-' ? '+' : '-');
		}

		cout << "Case #" << k << ": "; (ans < 0) ? cout << "IMPOSSIBLE" : cout << ans; cout << endl;
	}

	cin.close();
	cout.close();
	return 0;
}