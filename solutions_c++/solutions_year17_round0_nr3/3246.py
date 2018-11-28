#include <iostream>
#include <numeric>
#include <vector>

using namespace std;

int main() {
	int T;
	cin >> T;
	for(int t = 1; t <= T; t++) {
		long N, K;
		cin >> N >> K;
		vector<long> val{N}, cnt{1};
		bool found = false;
		while(true) {
			if(accumulate(cnt.begin(), cnt.end(), (long) 0) >= K) {
				long result = val[0];
				if(cnt[0] < K)
					result = val[1];
				result--;
				printf("Case #%d: %ld %ld\n", t, (result / 2) + (result % 2), result / 2);
				break;
			}
			else {
				K -= accumulate(cnt.begin(), cnt.end(), (long) 0);
				vector<long> nxt_val{val[0] / 2, val[0] / 2 - 1}, nxt_cnt(2);
				for(int i = 0; i < val.size(); i++) {
					if(val[i] % 2 == 1) {
						if(val[i] / 2 == nxt_val[0]) nxt_cnt[0] += cnt[i] * 2;	
						else nxt_cnt[1] += cnt[i] * 2;
					}
					else {
						nxt_cnt[0] += cnt[i];
						nxt_cnt[1] += cnt[i];
					}
				}
				val = nxt_val;
				cnt = nxt_cnt;
			}
		}
	}
}
