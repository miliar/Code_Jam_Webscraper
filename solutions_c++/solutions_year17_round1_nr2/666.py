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

		int arr[n][p];
		int grams[n];
		for (int i = 0; i < n; i++) {
			cin >> grams[i];
		}

		int last[n];

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < p; j++) {
				cin >> arr[i][j];
			}
			last[i] = 0;

			sort(arr[i], arr[i] + p);
		}
		int ans = 0;

		for (int i = 1;; i++) {
			int low[n];
			int mn = INT_MAX;

			for (int j = 0; j < n; j++) {
				int l = 9 * grams[j] * i;
				l = (l % 10) ? l / 10 + 1 : l / 10;

				int r = 11 * grams[j] * i / 10;

				low[j] = lower_bound(arr[j], arr[j] + p, l) - arr[j];
				int b = upper_bound(arr[j], arr[j] + p, r) - arr[j];

				low[j] = max(last[j], low[j]);

				if (low[j] == p) {
					goto FUCK;
				}

				int dist = b - low[j];

				if (dist <= 0) {
					goto DONE;
				}

				mn = min(dist, mn);
			}

			ans += mn;
			for (int j = 0; j < n; j++) {
				last[j] = low[j] + mn;
			}

			DONE:;
		}
		FUCK:;

		cout << ans << endl;
	}


	return 0;
}