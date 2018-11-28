#include <bits/stdc++.h>
using namespace std;

int TC, K;
string S;
set<int> req;

int main() {
	scanf("%d", &TC);
	for (int tc = 1; tc <= TC; tc++) {
		cin >> S >> K;
		int N = S.length();
		req.clear();
		if (S[0] == '-') req.insert(0);
		for (int i = 1; i < N; i++) {
			if (S[i - 1] != S[i]) req.insert(i);
		}
		if (S[N - 1] == '-') req.insert(N);
		int ans = 0;
		bool fail = 0;
		for (set<int>::iterator it = req.begin(); it != req.end(); it = req.begin()) {
			int val = *it;
			int target = *it + K;
			if (req.find(target) != req.end()) {
				ans++;
				req.erase(val);
				req.erase(target);
			} else {
				ans++;
				req.erase(val);
				req.insert(target);
				if (target > N) {
					fail = 1;
					break;
				}
			}
		}
		if (fail) printf("Case #%d: IMPOSSIBLE\n", tc);
		else printf("Case #%d: %d\n", tc, ans);
	}
}
