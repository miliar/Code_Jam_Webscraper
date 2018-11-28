#include <iostream>
#include <string>
#include <set>

using namespace std;

void flip(string& s, int p, int k) {
	for (int i = p; i < p + k; ++i) {
		if (s[i] == '-') s[i] = '+';
		else s[i] = '-';
	}
}

int main(){
	int t;
	cin >> t;
	for (int i = 1; i <= t; ++i) {
		string s;
		int k;
		cin >> s >> k;
		int res = 0;
		int len = s.size();

		for (int p = 0; p < len; ++p) {
			if (s[p] == '-') {
				if (p <= len-k) {
					++res;
					flip(s, p, k);
				} else {
					res = -1;
					break;
				}
			}
		}

		cout << "Case #" << i << ": ";
		if (res != -1) cout << res << endl;
		else cout << "IMPOSSIBLE" << endl;
	}

	return 0;
}
