#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	int T; cin >> T;
	for (int No = 1; No <= T; No++) {
		int N, P; cin >> N >> P;
		vector<int> G(N);
		for (int i = 0; i < N; i++) cin >> G[i];
		
		vector<int> count(P);
		for (int i = 0; i < N; i++) {
			count[G[i] % P]++;
		}

		int ans;
		if (P == 2) {
			ans = N - count[1] / 2;
		} else if (P == 3) {
			int a = count[1], b = count[2];
			int c = abs(a - b);
			ans = N - min(a, b) - (c - (c + 2) / 3);
		} else if (P == 4) {
			int a = count[1], b = count[2], c = count[3];
			ans = N - min(a, c) - b / 2;
			int d = abs(a - c), e = b % 2;
			if (e) {
				if (d <= 2) {
					ans -= d;
				} else {
					int d2 = d - 2;
					ans -= 2 + (d2 - (d2 + 3) / 4);
				}
			} else {
				ans -= (d - (d + 3) / 4);
			}
		} else {
			ans = -1;
		}

		cout << "Case #" << No << ": " << ans << endl;
	}
	return 0;
}
