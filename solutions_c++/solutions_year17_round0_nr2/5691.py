#include <bits/stdc++.h>
#define pb push_back
using namespace std;

int T;
string s;
int n;

int main() {
	cin >> T;
	for (int tc = 0; tc < T; tc++) {
		cin >> s;
		n = s.size();
		bool ok = true;
		for (int i = 0; i < n; i++) {
			if (!ok) s[i] = '9';
			else {
				if (i > 0 && s[i] < s[i - 1]) {
					ok = false;
					char d = s[i - 1] - 1;
					while (i > 0 && s[i] < s[i - 1]) {
						s[i - 1]--;
						i--;
					}
				}
			}
		}
		reverse(s.begin(), s.end());
		while (s.back() == '0') s.pop_back();
		reverse(s.begin(), s.end());
		cout << "Case #" << tc + 1 << ": ";
		cout << s << endl;
	}
	return 0;
}