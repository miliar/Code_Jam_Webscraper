# include <bits/stdc++.h>
using namespace std;

const int64_t LIM = 2e18;

int main()
{		
	int T; cin >> T;
	for(int tt=1; tt<=T; ++tt) {
		int64_t n, k; cin >> n >> k;
		
		priority_queue<int64_t> que;
		map<int64_t, int64_t> bath;
		
		que.push(n);
		bath[n] = 1;
		
		int64_t ls = -1, rs = -2;
		while(k) {
			int64_t lr = que.top(); que.pop();
			if (bath[lr] >= k) {
				ls = lr / 2;
				rs = (lr - 1) / 2;
				k = 0;
			}
			else {
				k -= bath[lr];
				
				int64_t ls_ = lr / 2;
				int64_t rs_ = (lr - 1) / 2;
				
				if (bath[ls_] == 0) que.push(ls_);
				bath[ls_] = min(bath[ls_] + bath[lr], LIM);
				
				if (bath[rs_] == 0) que.push(rs_);
				bath[rs_] = min(bath[rs_] + bath[lr], LIM);
			}
		}
		
		printf("Case #%d: %lld %lld\n", tt, ls, rs);
	}
	return 0;
}