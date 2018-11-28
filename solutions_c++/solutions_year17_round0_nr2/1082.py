#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <iostream>
#include <utility>
#include <set>
#include <cctype>
#include <queue>
#include <stack>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>

using namespace std;

int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		string s;
		cin >> s;

		int n = s.size();
		int idx = 0;
		bool isDec = false;
		for (int i = 1; i < n; i++) {
			if (s[i] > s[i - 1]) {
				idx = i;
			} else if (s[i] < s[i - 1]) {
				isDec = true;
				break;
			}
		}
		if (isDec) {
			string ret = s.substr(0, idx);
			if (s[idx] == '1') {
				for (int i = 0; i < n - 1; i++) {
					ret += '9';
				}
			} else {
				ret += (s[idx] - 1);
				for (int i = 0; i < n - idx - 1; i++) {
					ret += '9';
				}
			}
			cout << "Case #" << t << ": " << ret << endl;
		} else {
			cout << "Case #" << t << ": " << s << endl;
		}
	}
}

