#include <bits/stdc++.h>

using namespace std;

int main() {
	int i, j, n, a = 0, k, ct;
	string s;
	for (cin >> n; a < n;) {
		cin >> s >> k;
		for (ct = i = 0; i + k <= s.size(); i++) {
			if (s[i] != '-')
				continue;
			ct++;
			for (j = 0; j < k; j++)
				s[i + j] = s[i + j] == '-' ? '+' : '-';
		}
		for (; i < s.size(); i++)
			if (s[i] != '+')
				break;
		if (i == s.size())
			printf("Case #%d: %d\n", ++a, ct);
		else
			printf("Case #%d: IMPOSSIBLE\n", ++a);
	}
}