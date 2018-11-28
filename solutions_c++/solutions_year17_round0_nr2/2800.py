#include <iostream>
#include <vector>

using namespace std;

typedef long long ll;

void solve(int test) {
	cout << "Case #" << test << ": ";
	ll n;
	cin >> n;
	vector <ll> a(10);
	for (int i = 0; i < 10; i++) {
		for (int j = 0; j < 18; j++) {
			a[i] = a[i] * 10 + i;
		}
	}

	ll ans = 0;

	vector <ll> ten(19);
	
	ten[0] = 1;
	
	for (int i = 1; i <= 18; i++) {
		ten[i] = ten[i-1] * 10;
	}

	for (int i = 17; i >= 0; i--) {
		int num = 0;
		for (int cand = 0; cand < 10; cand++) {
			if (ans + a[cand] <= n) {
				num = cand;
			}
			a[cand] /= 10;
		}
		ans += ten[i] * num;
	}
	cout << ans << "\n";
}

int main() {
#ifdef KOBRA
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
#endif
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		solve(i);
	}
	return 0;
}

