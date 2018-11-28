#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;

using ll = long long;

ll const INF = 1000000000;



int main(void) {

	ios::sync_with_stdio(false);

	ifstream cin("input.txt");
	ofstream cout("output.txt");

	int T;
	cin >> T;

	for (int test = 1; test <= T; test++) {

		string s;
		cin >> s;
		int k, ans = 0;
		cin >> k;

		for (int i = 0; i < s.length(); i++) {
			if (i > s.length() - k) break;
			if (s[i] == '+') continue;
			ans++;
			for (int j = i; j < i + k; j++) {
				if (s[j] == '+') {
					s[j] = '-';
				}
				else {
					s[j] = '+';
				}
			}
		}
		bool flag = false;
		for (int i = 0; i < s.length(); i++) {
			if (s[i] == '-') {
				cout << "Case #" << test << ": IMPOSSIBLE\n";
				flag = true;
				break;
			}
		}

		if (flag) continue;
		cout << "Case #" << test << ": " << ans << "\n";
	}

	return 0;
}