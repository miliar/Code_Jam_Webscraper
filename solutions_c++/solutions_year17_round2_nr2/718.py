#include <bits/stdc++.h>
using namespace std;

int T;
const string impossible = "IMPOSSIBLE";

int main() {
	cin >> T;
	for (int t=1; t<=T; t++) {
		int N, R, O, Y, G, B, V;
		cin >> N >> R >> O >> Y >> G >> B >> V;
		string ans;
		if (R > N/2 || Y > N/2 || B > N/2)
			ans = impossible;
		else {
			int cnt[3];
			char tp[4] = "RYB";
			cnt[0] = R;
			cnt[1] = Y;
			cnt[2] = B;
			char last = 0;
			for (int i=0; i<N; i++) {
				int m = -1; 
				for (int j=0; j<3; j++)
					if (last != tp[j] && (m == -1 || cnt[j] > cnt[m]))
						m = j;
				if (m == -1) {
					ans = impossible;
					break;
				}
				else {
					ans += tp[m];
					cnt[m]--;
					last = tp[m];
				}
			}
		}
		if (ans != impossible && ans[0] == ans[N - 1]) {
			if (ans[N-3] != ans[N-1])
				swap(ans[N-1], ans[N-2]);
		}

		cout << "Case #" << t << ": " << ans << endl;

		if (ans != impossible && ans[0] == ans[N - 1]) {
			printf("\nERR!!!: \n");
			printf("N=%d  R=%d Y=%d B=%d\n", N, R, Y, B);
		}
	}
}
