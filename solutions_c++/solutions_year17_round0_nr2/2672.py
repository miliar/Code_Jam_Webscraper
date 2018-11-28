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
	ios_base::sync_with_stdio(false);
	cin.tie(0);

	int t;
	cin >> t;

	for (int cas = 1; cas <= t; cas++) {
		cout << "Case #" << cas << ": ";

		ll n;
		cin >> n;

		ll p = 1;
		ll tens = 1;
		ll ans = 0;

		while (p <= n) {
			p = p * 10 + 1;
			tens *= 10;
		}

		while (p > 1) {
			p /= 10;
			tens /= 10;

			int dig = 9;

			while (ans + dig * p > n) {
				--dig;
			}

			ans += tens * dig;
		}

		cout << ans << endl;
	}

	return 0;
}