#include <bits/stdc++.h>


#define ff first
#define ss second
#define puba push_back


using namespace std;


typedef long long LL;
typedef pair<int, int> pii;


const int MAXN = 110;


int a[MAXN];

int main() {
	int t;
	cin >> t;
	for (int q = 0; q < t; ++q) {
		cout << "Case #" << q + 1 << ": ";
		int n, p;
		cin >> n >> p;

		vector<int> mods(4, 0);
		for (int i = 0; i < n; ++i) {
			cin >> a[i];
			mods[a[i] % p]++;

		}
		
		if (p == 2) {
			cout << mods[0] + (mods[1] + 1) / 2;
		}
		if (p == 3) {
			int ans = mods[0];
			int mn = min(mods[1], mods[2]);
			ans += mn;
			mods[1] -= mn;
			mods[2] -= mn;

			ans += (mods[1] + mods[2] + 2) / 3;
			cout << ans;
		}

		if (p == 4) {
			int ans = mods[0];
			ans += mods[2] / 2;
			mods[2] %= 2;
			int mn = min(mods[1], mods[3]);
			ans += mn;
			mods[1] -= mn;
			mods[3] -= mn;
			int s = mods[1] + mods[3];

			if (mods[2] == 1 && s >= 2) {
				ans++;
				mods[2] = 0;
				s -= 2;
			}	
			if (mods[2] == 0) {
				ans += (s + 3) / 4;
			}
			else {
				ans++;
			}

			cout << ans;
		}

		cout << endl;
	}	
	return 0;
}