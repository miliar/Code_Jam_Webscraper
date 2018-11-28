#include <bits/stdc++.h>

using namespace std;

int solve() {
	string s;
	cin >> s;
	int k;
	cin >> k;

	int cnt = 0;

	for (int i = 0; i < s.size()-k+1; i++) {
		if (s[i] == '-') {
			for (int j = i; j < i+k; j++) {
				if (s[j] == '+') {
					s[j] = '-';
				} else if (s[j] == '-') {
					s[j] = '+';
				} else {
					assert(false);
				}
			}
			cnt++;
		}
	}

	for (int i = 0; i < s.size(); i++) {
		if (s[i] == '-') {
			return -1;
		}
	}

	return cnt;
}

void report(int test_num, int ans) {
	printf("Case #%d: ", test_num);
	if (ans == -1) {
		puts("IMPOSSIBLE");
	} else {
		printf("%d\n", ans);
	}
}

int main(void) {

	ios_base::sync_with_stdio (false);
	cin.tie(nullptr); 

	int t;
	cin >> t;

	for (int i = 0; i < t; i++) {
		report(i+1, solve());
	}

	return 0;
}