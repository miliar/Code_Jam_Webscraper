#include<bits/stdc++.h>
using LL= long long;
int main()
{
	int T;
	LL n, K;
	freopen("C-large.in", "r", stdin);
	freopen("data.out", "w", stdout);
	std::cin >> T;
	for(int t = 1; t <= T; t ++) {
		std::cin >> n >> K;
		std::cout << "Case #" << t << ": ";
		std::set<LL> st;
		std::map<LL, LL> mp;

		st.insert(n);
		mp[n] = 1LL;

		LL ans1 = -1, ans2 = -1;
		LL cnt = 0;
		while(cnt < K) {
			auto it = --st.end();
			LL val = *it;
			LL ret = mp[val];
			ans1 = (val - 1) / 2;
			ans2 = val - 1 - ans1;
			if(ret + cnt >= K) {
				break;
			}
			cnt += ret;
			st.erase(it);

			//std::cout << "han " << cnt << " " << ans1 << " " << ans2 << " " << val << " " << ret << std::endl;

			mp[val] = 0;
			if(ans1 != 0) {
				mp[ans1] += ret;
				st.insert(ans1);
			}
			if(ans2 != 0) {
				mp[ans2] += ret;
				st.insert(ans2);
			}
		}
		std::cout << std::max(ans1, ans2) << " " << std::min(ans1, ans2) << std::endl;
	}
	return 0;
}
