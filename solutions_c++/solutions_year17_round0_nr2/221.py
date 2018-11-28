#include <bits/stdc++.h>
using namespace std;

char s[25];

void solve() {
	scanf("%s", s);
	int n = strlen(s);
	int last = 0, lastp = -1, i = 0;
	while (i < n) {
		int d = s[i] - '0';
		if (d > last) {
			last = d;
			lastp = i;
			i++;
		} else if (d == last) {
			i++;
		} else {
			s[lastp]--;
			for (i = lastp+1; i < n; i++) s[i] = '9';
		}
	}
	lastp = 0;
	while (s[lastp] == '0') lastp++;
	printf("%s\n", s+lastp);
}

int main() {
	freopen("B.out", "w", stdout);
	int t; scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		printf("Case #%d: ", i);
		solve();
	}
}