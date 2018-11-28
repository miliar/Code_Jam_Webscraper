#include <bits/stdc++.h>

using namespace std;
const int N = 1001;
string greedy(char a[], int k) {
	string s(a);
	int ret = 0;
	for (int i = 0; i < s.size(); ++i) {
		if (s[i] == '-') {
			for (int j = 0; j < k; ++j) {
				if (i + j >= s.size())
					return "IMPOSSIBLE";
				if (s[i + j] == '+') {
					s[i + j] = '-';
				} else {
					s[i + j] = '+';
				}
			}
			++ret;
		}
	}
	return to_string(ret);
}
int main() {
#ifndef ONLINE_JUDGE
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);
#endif
	int t;
	scanf("%d\n", &t);
	for (int test = 1; test <= t; ++test) {
		char s[N];
		int k;
		scanf("%s %d\n", s, &k);
		printf("Case #%d: %s\n", test, greedy(s, k).c_str());
	}
	
	
	return 0;
}

