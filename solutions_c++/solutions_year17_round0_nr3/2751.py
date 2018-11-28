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

map<ll, ll> mp;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);

	int t;
	cin >> t;

	for (int cas = 1; cas <= t; cas++) {
		cout << "Case #" << cas << ": ";

		ll n, k;
		cin >> n >> k;

		mp.clear();

		ll cnt = 1;
		--n;

		while (k > cnt) {
			mp[n - n / 2] += cnt;
			mp[n / 2] += cnt;
			k -= cnt;

			pair<ll, ll> p = *mp.rbegin();

			n = p.first;
			cnt = p.second;
			mp.erase(n);
			--n;
		}

		cout << n - n / 2 << " " << n / 2 << endl;
	}

	return 0;
}