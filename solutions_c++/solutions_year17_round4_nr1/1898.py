#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
int main() {
	freopen("A-small-attempt3.in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int cases;
	cin >> cases;
	for (int cas = 1; cas <= cases; cas++) {
		int N, P;
		cin >> N >> P;
		vector<int> G(N);
		int ans = 0;
		int ones = 0, twos = 0, threes = 0;
		for (int i = 0; i < N; i++) {
			cin >> G[i];
			G[i] %= P;
			if (G[i] == 0) ans++;
			if (G[i] == 1) ones++;
			if (G[i] == 2) twos++;
			if (G[i] == 3) threes++;
		}
		if (P == 2) {
			ans += (ones + 1) / 2;
		}
		if (P == 3) {
			int t = min(ones, twos);
			ans += t;
			ones -= t;
			twos -= t;
			if (ones) {
				ans += ones / 3;
				ones %= 3;
			}
			else {
				if (twos) {
					ans += twos / 3;
					twos %= 3;
				}
			}
			if (ones || twos) {
				ans ++;
			}
		}
		if (P == 4) {
			int t = min(ones, threes);
			ans += t;
			ones -= t;
			threes -= t;
			if (ones) {
				//有1 没3
				if (ones && twos) {
					t = min(ones / 2, twos);
					ans += t;
					ones -= t * 2;
					twos -= t;
				}
				if (twos) {
					ans += twos / 2;
					twos %= 2;
				}
			}
			else {
				if (threes) {
					ans += threes / 4;
					threes %= 4;
				}
				if (twos) {
					ans += twos / 2;
					twos %= 2;
				}
			}
			if (ones || twos || threes) ans ++;
		}
		

		cout << "Case #"<<cas<<": ";
		cout << ans << endl;	
	}
	


	return 0;
}