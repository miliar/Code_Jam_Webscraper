#include <bits/stdc++.h>
using namespace std;

#define for_(i,a,b) for(int i=(a);i<(b);++i)
#define for_rev(i,a,b) for(int i=(a);i>=(b);--i)
typedef long long lint;

void solve() {
	lint N;
	cin >> N;
	
	stringstream ss; ss << N;
	int digits = ss.str().size();
	lint ans = 0;
	
	for_(i,0,digits) {
		lint last_number = ans % 10;
		for_rev(x,9,last_number) {
			lint sub_ans = ans;
			for_(j,0,digits-i) sub_ans = 10 * sub_ans + x;
			if (sub_ans <= N) {
				ans = 10 * ans + x;
				break;
			}
		}
	}
	
	cout << ans << endl;
}

int main() {
	int T;
	cin >> T;
	
	for_(i,0,T) {
		cout << "Case #" << i + 1 << ": ";
		solve();
	}
}