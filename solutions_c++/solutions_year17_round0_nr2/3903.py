#include <cstdio>
#include <iostream>
#include <cstring>

using namespace std;

int t;
string s;

int main() {
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);

	cin >> t;
	for (int it = 1; it <= t; ++it) {
		cin >> s;
		int n = s.length(), pos = -1; 
		for (int i = 0; i < n - 1; ++i) {
			if (s[i + 1] < s[i]) {
				pos = i;
				break;
			}
		}

		printf("Case #%d: ", it);
		if (pos == -1) {
			cout << s << '\n';
		} else {
			s[pos]--;
			while (pos > 0 && s[pos - 1] > s[pos]) {
				pos--;
				s[pos]--;
			}

			for (int i = pos + 1; i < n; ++i)
				s[i] = '9';
			pos = 0;
			while (s[pos] == '0')
				pos++;
			for (int i = pos; i < n; ++i)
				printf("%c", s[i]);
			printf("\n");
		}
	}
}