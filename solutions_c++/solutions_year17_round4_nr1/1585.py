#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

int main()
{
	int T; cin >> T;
	for (int t = 0; t < T; t++) {
		cout << "Case #" << t + 1 << ": ";

		int N, P; cin >> N >> P;

		vector<int>G(N);
		for (int i = 0; i < N; i++) {
			cin >> G[i];
			G[i] %= P;
		}

		vector<int>cnt(4);
		for (int i = 0; i < N; i++) {
			cnt[G[i]]++;
		}

		int ans = 0;
		ans += cnt[0];
		if (P == 2) {
			ans += cnt[1] / 2;
			cnt[1] %= 2;
			ans += ceil(cnt[1] / 2.);
		}
		else if (P == 3) {
			ans += min(cnt[1], cnt[2]);
			int tmp = min(cnt[1], cnt[2]);
			cnt[1] -= tmp;
			cnt[2] -= tmp;
			ans += cnt[1] / 3;
			ans += cnt[2] / 3;
			cnt[1] %= 3;
			cnt[2] %= 3;
			ans += ceil(cnt[1] / 3.);
			ans += ceil(cnt[2] / 3.);
		}
		else if (P == 4) {
			ans += cnt[2]/2 + min(cnt[1], cnt[3]);
			int tmp = min(cnt[1], cnt[3]);
			cnt[1] -= tmp;
			cnt[2] %= 2;
			cnt[3] -= tmp;
			ans += cnt[1] / 4;
			ans += cnt[3] / 4;
			cnt[1] %= 4;
			cnt[3] %= 4;
			if (cnt[2]) {
				if (cnt[1]) {
					if (cnt[1] <= 2)ans += 1;
					else ans += 2;
				}
				else if (cnt[3]) {
					if (cnt[3] <= 2)ans += 1;
					else ans += 2;
				}
			}
			else {
				ans += ceil(cnt[1] / 4.);
				ans += ceil(cnt[3] / 4.);
			}
		}

		cout << ans << endl;
	}

    return 0;
}

