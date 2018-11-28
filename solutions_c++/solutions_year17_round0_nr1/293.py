#include <iostream>
#include <algorithm>
#include <vector>
#include <math.h>
#include <stdio.h>
#include <string>
using namespace std;

void solve(int test) {
	string s;
	int k;
	cin >> s >> k;
	int num = 0;
	for (int i = 0; i < s.length(); ++i) {
		if (s[i] == '-') {
			++num;
			if (i + k > s.length()) {
				printf("Case #%d: IMPOSSIBLE\n", test);
				return;
			}
			for (int j = i; j < i + k; ++j) {
				if (s[j] == '-') s[j] = '+';
				else s[j] = '-';
			}
		}
	}
	printf("Case #%d: %d\n", test, num);
}

int main()
{
	freopen("in.in", "r", stdin);
	freopen("out.out", "w", stdout);
	int T;
	cin >> T;
	for (int i = 0; i < T; ++i)
		solve(i + 1);
	return 0;
}