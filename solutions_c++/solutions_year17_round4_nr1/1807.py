#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;
typedef vector<int> vi;

int main(){
	ios::sync_with_stdio(0);

	int T; cin >> T;
	for(int id = 1; id <= T; id++) {
		int N, P; cin >> N >> P;
		cout << "Case #" << id << ": ";
		vector<int> nums;
		for(int i = 0; i < N; i++) {
			int curr; cin >> curr; nums.push_back(curr);
		}

		if(P == 2) {
			int ans = 0, tmpAns = 0;
			for(int i : nums) {
				if(i % 2 == 0) {
					ans++;
				} else {
					tmpAns++;
				}
			}

			cout << ans + ((tmpAns + 1) / 2) << endl;
		} else if (P == 3) {
			int ans = 0;
			vector<int> newNums1, newNums2;
			for(int num : nums) {
				if(num % 3 == 0) {
					ans++;
				} else if(num % 3 == 1) {
					newNums1.push_back(num);
				} else {
					newNums2.push_back(num);
				}
			}

			ans += min(newNums1.size(), newNums2.size());
			if(newNums1.size() > newNums2.size()) {
				ans += 1 + (newNums1.size() - newNums2.size() -1) / 3;
			} else if (newNums2.size() > newNums1.size()) {
				ans += 1 + (newNums2.size() - newNums1.size() - 1) / 3;
			}
			cout << ans << endl;
		}
	}
	
	return 0;
}