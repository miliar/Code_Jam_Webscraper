#include<iostream>
#include<string>
using namespace std;
int n, t, k, l, r, a, j, i;
bool m;
string s;
int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> t;
	while (j++ < t) {
		cin >> s >> k;
		n = s.length();
		a = m = 0;
		for (int i = 0; i < n;++i) {
			if (s[i] == '-') {
				++a;
				for (int u = i + 1; u < i + k; ++u)
					if (u < n)s[u] = '+' + '-' - s[u];
					else m = 1;
			}
		}
		cout << "Case #" << j << ": ";
		if (m)cout << "IMPOSSIBLE\n";
		else cout << a << endl;
	}
}