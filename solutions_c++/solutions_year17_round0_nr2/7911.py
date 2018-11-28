#include <bits/stdc++.h>
using namespace std;
inline bool check(string &st) {
	for (int i = 1; i < st.size(); i++) {
		if (st[i - 1] > st[i]) {
			return false;
		}
	}
	return true;
}
int main() {
	int T;
	cin >> T;
	for (int test = 1; test <= T; test++) {
		string st;
		cin >> st;
		cout << "Case #" << test << ": ";
		while (!check(st)) {
			for (int i = 1; i < st.size(); i++) {
				if (st[i - 1] > st[i]) {
					if (st[i - 1] != '0') {
						st[i - 1]--;
						for (int j = i; j < st.size(); j++) {
							st[j] = '9';
						}
					} else {
						int cur = i - 1;
						while (true) {
							if (st[cur] == '0') {
								cur--;
							} else {
								st[cur]--;
								break;
							}
						}
						for (int j = cur + 1; j < st.size(); j++) {
							st[j] = '9';
						}
					}
					break;
				}
			}
			if (st[0] == '0') {
				st.erase(st.begin());
			}
		}
		cout << st << '\n';

	}
}
