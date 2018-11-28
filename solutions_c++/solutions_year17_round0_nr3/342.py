#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

ll f(ll K, ll N) {
	//cout << "K,N = " << K << " " << N << endl;
	int p = 0;
	while (((1LL)<<(p+1)) - 1 < K) {
		p++;
	}
	ll taken = ((1LL)<<p) - 1;
	//cout << "taken = " << taken << endl;
	ll m = N - taken; // # remaining cells
	ll l = m / ((1LL)<<p); // each cell is either l or l+1 in length
	ll rem = m - l * ((1LL)<<p);
	//cout << "l = " << l << endl;
	//cout << "m,rem = " << m << " " << rem << endl;
	if (rem == 0) {
		return l;
	}
	if (taken+rem >= K) {
		return l+1;
	}
	return l;
}

int main() {
	int ncases;
	cin >> ncases;
	for (int icase = 1; icase <= ncases; icase++) {
		ll K, N;
		cin >> N >> K;
		ll lastSplit = f(K, N);
		//cout << "last = " << lastSplit << endl;
		lastSplit--;
		ll a = lastSplit/2;
		ll b = lastSplit - a;
		cout << "Case #" << icase << ": " << b << " " << a << endl;
	}
	return 0;
}
