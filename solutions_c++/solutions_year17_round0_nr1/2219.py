#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <string>

using namespace std;

void invert(string & s, int i, int l) {
	for (int j = i; j < i + l; j++) {
		s[j] = s[j] == '-' ? '+' : '-';
	}
}

int main() {
	ios::sync_with_stdio(false);

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t;
	cin >> t;
	for (int i = 0; i < t; i++) {
		string s;
		int k;
		cin >> s >> k;
		bool f = false;
		int ans = 0;
		for (int i = 0; i < s.size(); i++) {
			if (s[i] == '-') {
				if (i + k > s.size()) {
					f = true;
					break;
				}
				invert(s, i, k);
				ans++;
			}
		}
		cout << "Case #" << i + 1 << ": ";
		if (f) {
			cout << "IMPOSSIBLE";
		}
		else {
			cout << ans;
		}
		cout << endl;
	}
}