#include <bits/stdc++.h>
using namespace std;
int main() {
	string s;
	int cs, t, i, j, a, k;
	cin >> t;
	for (cs = 1; cs <= t; ++cs) {
		a = 0;
		cin >> s >> k;
		for (i = 0; i < s.size() - k + 1; ++i)
			if (s[i] == '-')
				for (j = 0, ++a; j < k; ++j) s[i + j] = '+' + '-' - s[i + j];
		for (; i < s.size(); ++i)
			if (s[i] == '-') break;
		cout << "Case #" << cs << ": " << (i < s.size() ? "IMPOSSIBLE" : to_string(a)) << endl;
	}
	return 0;
}
