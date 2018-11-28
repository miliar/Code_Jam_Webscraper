#include <bits/stdc++.h>
using namespace std;
int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
	int t;
	cin >> t;
	for (int j = 0; j < t; j++) {
		int n;
		int R, O, Y, G, B, V;
		cin >> n;
		cin >> R >> O >> Y >> G >> B >> V;
		string ans, ans1, ans2;
		int tmpR = R, tmpB = B, tmpY = Y;
		for (int i = 0; i < n; i++) {
			if ((!i || (i && ans[i - 1] != 'R')) && R >= B && R >= Y && R > 0) {
				R--;
				ans += 'R';
			} else if ((!i || (i && ans[i - 1] != 'B')) && B >= Y && B > 0) {
				B--;
				ans += 'B';

			} else if ((!i || (i && ans[i - 1] != 'Y')) && Y > 0) {
				Y--;
				ans += 'Y';
			}
		}
		R = tmpR, B = tmpB, Y = tmpY;
		for (int i = 0; i < n; i++) {
			if ((!i || (i && ans1[i - 1] != 'B')) && B >= Y && B >= R
					&& B > 0) {
				B--;
				ans1 += 'B';

			} else if ((!i || (i && ans1[i - 1] != 'R')) && R >= Y && R > 0) {
				R--;
				ans1 += 'R';
			} else if ((!i || (i && ans1[i - 1] != 'Y')) && Y > 0) {
				Y--;
				ans1 += 'Y';
			}
		}
		R = tmpR, B = tmpB, Y = tmpY;
		for (int i = 0; i < n; i++) {
			if ((!i || (i && ans2[i - 1] != 'Y')) && Y >= B && Y >= R
					&& Y > 0) {
				Y--;
				ans2 += 'Y';
			} else if ((!i || (i && ans2[i - 1] != 'R')) && R >= B && R > 0) {
				R--;
				ans2 += 'R';
			} else if ((!i || (i && ans2[i - 1] != 'B')) && B > 0) {
				B--;
				ans2 += 'B';

			}
		}
		///cout << ans << endl << ans1 << endl << ans2 << endl;
		if ((int) ans.size() == n && ans[(int) ans.size() - 1] != ans[0]) {
			cout << "Case #" << j + 1 << ": " << ans << endl;
		} else if ((int) ans1.size() == n
				&& ans1[(int) ans1.size() - 1] != ans1[0]) {
			cout << "Case #" << j + 1 << ": " << ans1 << endl;
		} else if ((int) ans2.size() == n
				&& ans2[(int) ans2.size() - 1] != ans2[0]) {
			cout << "Case #" << j + 1 << ": " << ans2 << endl;
		} else {
			cout << "Case #" << j + 1 << ": IMPOSSIBLE" << endl;
		}
	}
}

