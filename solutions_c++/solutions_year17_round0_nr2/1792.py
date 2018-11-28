#include <bits/stdc++.h>
#define ll long long
using namespace std;
void solve() {
	ll n;
	cin >> n;
	ll d = 10;
	while (n / d) {
		if ((n/d)%10 > n/(d/10)%10) {
			n = n/d*d-1;
		}
		d *= 10;
	}
	cout << n << endl;
	return;
}
int main() {
	int t;
	cin >> t;
	for (int i=0;i<t;i++) {
		cout << "Case #" << i+1 << ": ";
		solve();
	}
	return 0;
}