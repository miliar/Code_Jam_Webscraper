/* [theMighty] Deathsurgeon
* Rupesh Maity
* Final Year
* IIIT Allahabad
* In search of my ikigai
* Youtube Channel: https://www.youtube.com/channel/UCn1VDq6nXGUGdHVyxU2zFSw
*/

#include <bits/stdc++.h>

#define sd(x) scanf("%d", &x)
#define pb push_back
#define pii pair<int, int>
#define ll long long

#define MAX 1000001
#define MOD 1000000007
#define PI 3.141592653589793

using namespace std;

int main() {
	int t;
	cin >> t;

	for (int cas = 1; cas <= t; cas++) {
		cout << "Case #" << cas << ": ";

		int n, p;
		cin >> n >> p;

		int arr[n];

		for (int i = 0; i < n; i++) {
			cin >> arr[i];
		}

		if (p == 2) {
			int cnt[2] = {};

			for (int i = 0; i < n; i++) {
				++cnt[arr[i] % 2];
			}

			cout << cnt[0] + (cnt[1] + 1) / 2 << endl;
		} else if (p == 3) {
			int cnt[3] = {};

			for (int i = 0; i < n; i++) {
				++cnt[arr[i] % 3];
			}

			int ans = cnt[0] + min(cnt[1], cnt[2]);

			int lft = max(cnt[1], cnt[2]) - min(cnt[1], cnt[2]);

			cout << ans + lft / 3 + ((lft % 3)? 1 : 0) << endl;
		} else if (p == 4) {
			int cnt[4] = {};

			for (int i = 0; i < n; i++) {
				++cnt[arr[i] % 4];
			}

			int ans = cnt[0] + cnt[2] / 2;

			int a = cnt[2] % 2;

			ans += min(cnt[1], cnt[3]);

			int b = max(cnt[1], cnt[3]) - min(cnt[1], cnt[3]);


			if (a) {
				if (b > 1) {
					++ans;
					b -= 2;
					a = 0;
				}
			}

			ans += b / 4;

			b %= 4;

			if (a || b) {
				ans++;
			}

			cout << ans << endl;
		}
	}


	return 0;
}