#include <bits/stdc++.h>

int solve(std::string &s, int k) {
	int n = (int)s.size();
	
	int ans = 0;
	std::vector<int> a(n, 0);
	int count = 0;
	
	for (int i = 0; i < n; i++) {
		bool needAdd = false;
		if (s[i] == '-') {
			if (count % 2 == 0) {
				needAdd = true;
			}
		} else {
			if (count % 2 != 0) {
				needAdd = true;
			}
		}
		
		if (needAdd) {
			ans++;
			if (i + k - 1 < n) {
				count++;
				a[i + k - 1] = -1;
			} else {
				return -1;
			}
		}
		
		count += a[i];
	}
	
	if (count != 0) return -1;
		
	return ans;
}

int main() {
	int q; scanf("%d", &q);
	
	for (int i = 1; i <= q; i++) {
		std::string s; std::cin >> s;
		int k; scanf("%d", &k);
		
		int ans = solve(s, k);
		
		printf("Case #%d: ", i);
		if (ans == -1) {
			printf("IMPOSSIBLE");
		} else {
			printf("%d", ans);
		}
		printf("\n");
	}

	return 0;
}
