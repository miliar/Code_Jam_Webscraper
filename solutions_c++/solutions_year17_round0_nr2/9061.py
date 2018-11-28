#include <bits/stdc++.h>

using namespace std;
#define fr first
#define sc second
#define sz(c) int(c.size())
#define all(c) c.begin(), c.end()
#define rall(c) c.rbegin(), c.rend()
#define vlong long long

int main() {
	freopen("in.txt" , "r", stdin);
	freopen("out.txt" , "w", stdout);
	int t;
	cin >> t;
	int ts = 1;
	while (t--) {
		string s;
		cin >> s;
		for (int i = sz(s) - 1; i > 0; --i) {
			for (int j = i - 1; j >= 0; --j) {
				if ((s[i] - '0') < (s[j] - '0')) {
					for (int k = i; k < sz(s); ++k) {
						s[k] = '9';
					}
					s[i - 1]--;
					break;
				}
			}
		}
		int id = 0;
		for (int i = 0; i < sz(s); ++i) {
			if (s[i] != '0') {
				id = i;
				break;
			}
		}
		printf("Case #%d: ", ts);
		cout << s.substr(id) << endl;
		ts++;
	}

}
