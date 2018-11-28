#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <vector>

using namespace std;

typedef vector<int> vi;
typedef long long ll;

bool isTidy(int n) {
	int d = 9;
	while(n > 0) {
		if(n%10 > d) return false;
		if(n%10 < d) d = n%10;
		n/=10;
	}
	return true;
}

int getLastNaive(int n) {
	for(int m = n;m >= 1; --m) {
		if(isTidy(m)) return m;
	}
}

ll getLastSmart(ll n) {
	vi xs;
	while(n > 0) {
		xs.push_back(n%10);
		n /= 10;
	}
	xs = vi(xs.rbegin(), xs.rend());
	int k = (int)xs.size();
	vi ys(k);
	for(int i = 0;i < k; ++i) {
		bool good = true;
		for(int j = i;j < k;++j) {
			if(xs[j] > xs[i]) {
				j = k;
			} else if(xs[j] < xs[i]) {
				good = false;
			}
		}
		if(good) {
			ys[i] = xs[i];
		} else {
			ys[i] = xs[i]-1; //can never be -1
			for(int j = i+1;j < k; ++j) {
				ys[j] = 9;
			}
			i = k;
		}
	}
	ll m = 0;
	for(int i = 0; i < k; ++i) {
		m *= (ll)10;
		m += (ll)ys[i];
	}
	return m;
}

ll solve() {
	ll n;
	cin >> n;
	return getLastSmart(n);
}

int main() {
	int T;
	cin >> T;
	for(int t = 1;t <= T;++t) {
		ll s = solve();
		cout << "Case #" << t << ": ";
		cout << s;
		cout << endl;
	}
}