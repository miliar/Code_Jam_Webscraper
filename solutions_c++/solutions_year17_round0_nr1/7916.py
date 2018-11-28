#include <bits/stdc++.h>

#define sz(s) (int)s.size()
#define all(s) s.begin(),s.end()

typedef long long ll;
typedef unsigned long long ull;
using namespace std;

int main() {

#ifndef ONLINE_JUDGE
	//freopen("input.txt", "r", stdin);
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	int n;
	cin >> n;
	for (int i = 1; i <= n; i++) {
		cout << "Case #" << i << ": ";
		string s;
		int x, counter = 0, j;
		cin >> s >> x;
		for (j = 0; j <= sz(s) - x; j++) {
			if (s[j] == '-') {
				for (int k = 0; k < x; k++) {
					if (s[j + k] == '-')
						s[j + k] = '+';
					else
						s[j + k] = '-';
				}
				counter++;
			}
		}
		bool flag = true;
		for (; j < sz(s); j++) {
			if (s[j] != s[j - 1]) {
				flag = false;
				break;
			}
		}
		if (!flag) {
			cout << "IMPOSSIBLE" << endl;
		} else {
			if (s[sz(s) - 1] == '-')
				cout << counter + x << endl;
			else
				cout << counter << endl;
		}
	}

	return 0;
}
