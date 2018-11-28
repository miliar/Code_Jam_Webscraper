#define _CRT_SECURE_NO_WARNINGS

#include <vector>
#include <iostream>
#include <string>


using namespace std;

void solve_single() {
	string str;
	int k;
	cin >> str >> k;
	int ans = 0;
	for (int i = 0; i <= str.size() - k; ++i) {
		if (str[i] == '-') {
			ans++;
			for (int j = i; j < i + k; ++j) {
				if (str[j] == '-') {
					str[j] = '+';
				}
				else {
					str[j] = '-';
				}
			}
		}
	}
	for (int i = 0; i < str.size(); ++i) {
		if (str[i] != '+') {
			cout << "IMPOSSIBLE" << endl;
			return;
		}
	}
	cout << ans << endl;
	return;
}

int main () {
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	cin >> T;
	for (int i = 0; i < T; ++i) {
		cout << "Case #" << i + 1 << ": ";
		solve_single();
	}
	return 0;
};
