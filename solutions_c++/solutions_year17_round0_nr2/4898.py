#define _CRT_SECURE_NO_WARNINGS

#include <map>
#include <set>
#include <cmath>
#include <deque>
#include <queue>
#include <stack>
#include <cstdio>
#include <string>
#include <vector>
#include <complex>
#include <cstring>
#include <iomanip>
#include <utility>
#include <iostream>
#include <algorithm>

using namespace std;

int main() {

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	cin >> T;
	
	for(int t = 1; t <= T; t++) {
		string s;
		cin >> s;
		int n = s.length();
		for (int x = 0; x < 20; x++) {
			for (int i = 0; i + 1 < n; i++) {
				if (s[i] > s[i + 1]) {
					s[i]--;
					i++;
					while (i < n) {
						s[i] = '9';
						i++;
					}
				}
			}
		}
		long long ans = 0;
		for (int i = 0; i < n; i++) {
			ans *= 10LL;
			ans += s[i] - '0';
		}
		cout << "Case #" << t << ": " << ans << '\n';
	}

	return 0;
}