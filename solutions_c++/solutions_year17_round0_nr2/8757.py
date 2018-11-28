#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t, cas = 1;
	scanf("%d", &t);
	char s[25];
	while (t-- != 0) {
		printf("Case #%d: ", cas++);
		scanf("%s", s);
		int n = strlen(s), at = -1;
		for (int i = 1; i < n; ++i)
			if (s[i] < s[i - 1]) {
				at = i;
				break;
			}
		if (at == -1) {
			puts(s);
			continue;
		}
		bool ch[20] = { };
		for (int i = at - 1; i >= 0 && s[i] == s[at - 1]; --i)
			ch[i] = true;
		if (ch[0] && s[0] == '1') {
			puts(string(n - 1, '9').c_str());
			continue;
		}
		for (int i = 0; i < n; ++i)
			if (ch[i]) {
				--s[i];
				for (int j = i + 1; j < n; ++j)
					s[j] = '9';
				break;
			}
		puts(s);
	}
	return 0;
}
