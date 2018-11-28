#include <bits/stdc++.h>
#include <algorithm>
using std::min;
int main () {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int T; std::cin >> T; for (int TT = 0; TT < T; ++TT) {
		int n, p; std::cin >> n >> p;
		//std::cout << '\n' << p << '\n';
		int a[4];
		a[0] = a[1] = a[2] = a[3] = 0;
		for (int i = 0; i < n; ++i) {
			int meow; std::cin >> meow; ++a[meow % p];
			//std::cout << meow << ' '; 
		}
		int ans;
		if (p == 2) ans = a[0] + a[1] / 2 + a[1] % 2;
		if (p == 3) ans = a[0] + min(a[1], a[2]) + (a[1] + a[2] - 2 * min(a[1], a[2])) / 3 + !!((a[1] + a[2] - 2 * min(a[1], a[2])) % 3); 
		if (p == 4) ans = a[0] + a[2] / 2 + min(a[1], a[3]) + (a[1] + a[3] - 2 * min(a[1], a[3]) + 2 * (a[2] % 2)) / 4
		+ !!((a[1] + a[3] - 2 * min(a[1], a[3]) + 2 * (a[2] % 2)) % 4);
		std::cout << "Case #" << TT + 1 << ": " << ans << '\n'; 
	}
}
