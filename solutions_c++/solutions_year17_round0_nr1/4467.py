#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <string>

using namespace std;

char flip(char c) {
	if (c == '-') {
		return '+';
	}
	return '-';
}

int solve(string& str, int k) {
	int count = 0;
	for (int i = 0; i + k <= str.size(); ++i) {
		if (str[i] == '-') {
			for (int j = i; j < i+ k; ++j) {
				str[j] = flip(str[j]);
			}
			++count;
		}
	}
	
	for (int i = str.size() - k; i < str.size(); ++i) {
		if (str[i] == '-') {
			return -1;
		}
	}
	return count;
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("out.out", "w", stdout);
	int T;
	scanf("%d\n", &T);
	for (int cas = 1; cas <= T; ++cas) {
		string str;
		int k;
		cin >> str;
		scanf("%d\n", &k);
		int ans = solve(str, k);
		
		// printf("Solving for %s and %d\n", str.c_str(), k);
		
		// Output Solution
		printf("Case #%d: ", cas);
		if (ans == -1) {
			printf("IMPOSSIBLE\n");
		} else {
			printf("%d\n", ans);
		}
	}
	
	return 0;
}

