#include <bits/stdc++.h>
using namespace std;

int main() {
	//freopen("B-large.in", "r", stdin);
	//freopen("out.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int Case = 1; Case <= t; ++Case) {
		string s;
		int last = -1;
		cin >> s;
		for (int i = (int) s.size() - 2; i >= 0; --i) {
			if (s[i] > s[i + 1]) {
				s[i]--;
				last = i + 1;
			}
		}
		while (last < (int) s.size() && last != -1) {
			s[last++] = '9';
		}
		bool ok = false;
		printf("Case #%d: ", Case);
		for (int i = 0; i < (int) s.size(); ++i) {
			if (s[i] == '0' && !ok)
				continue;
			printf("%c", s[i]);
			ok = true;
		}
		if(Case<t)
			putchar('\n');
	}
	return 0;
}
