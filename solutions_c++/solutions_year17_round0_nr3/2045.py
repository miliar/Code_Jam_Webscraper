#include <bits/stdc++.h>
#define LL long long
using namespace std;

map<LL, LL> cnt;

void all_poss(LL n) {
	if(n == 0 || cnt[n] > 0) return ;
	cnt[n] = 1;
	LL a = (n-1)/2, b;
	b = (n - 1) - a;
	all_poss(a);
	all_poss(b);
}

int main() {
	srand(time(NULL));
	ios_base::sync_with_stdio(false);
	int t;
	LL n, k;
	cin >> t;
	for(int tc = 1; tc <= t; tc++) {
		cnt.clear();
		cin >> n >> k;
		all_poss(n);
		assert(cnt.size() > 0);
		auto it = prev(cnt.end());
		while(it != cnt.begin()) {
			it = prev(it);
			LL curr = it->first;
			cnt[curr] = 0;
			vector<LL> v = {2*curr, 2*curr + 1, 2*curr + 1, 2*curr + 2};
			for(auto &elem: v) {
				if(cnt.count(elem)) {
					cnt[curr] += cnt[elem];
				}
			}
			assert(cnt[curr] > 0);
		}
		LL taken = 0;
		it = prev(cnt.end());
		LL ans = -1;
		while(taken < k) {
			if(taken + it->second >= k) {
				ans = it->first;
				break;
			} else {
				taken += it->second;
				if(it == cnt.begin())
				assert(it != cnt.begin());
				it--;
			}
		}
		assert(ans != -1);
		LL a = (ans - 1)/2, b = (ans - 1 + 1)/2;
		cout << "Case #" << tc << ": " << b << ' ' << a << '\n';
	}
	return 0;
}
