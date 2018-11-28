#include <bits/stdc++.h>
using namespace std;
 
typedef long long LL;
typedef pair<LL, LL> II;

int main() {
	int TC; cin >> TC;
	for (int testID = 1; testID <= TC; ++testID) {
		printf("Case #%d: ", testID);
		LL n, k; cin >> n >> k;
		map<LL, LL> cnt; cnt[n] = 1;
		while (1) {
			LL L = cnt.rbegin()->first;
			LL C = cnt.rbegin()->second;
			LL l1 = (L + 1) / 2 - 1;
			LL l2 = L - l1 - 1;
			if (k <= C) {
				cout << max(l1, l2) << " " << min(l1, l2) << "\n";
				break;
			}
			else {
				k -= C; cnt.erase(L);
				cnt[l1] += C;
				cnt[l2] += C;
			}
		}
	}
	return 0;
}