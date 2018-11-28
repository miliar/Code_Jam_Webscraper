#include <bits/stdc++.h>

#define endl '\n'
#define eps 1e-9

using namespace std;

int main() {
	ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);
	int TestCase;
	cin >> TestCase;
	for(int TestNumber = 1; TestNumber <= TestCase; TestNumber++) {
		cout << "Case #" << TestNumber << ": ";
		long long D, n;
		cin >> D >> n;
		long double a[n];
		long long b[n];
		for(int i=0; i<n; i++) cin >> a[i] >> b[i];
		long double T = 0;
		for(int i=n-1; i>=0; i--) {
			a[i] += T*b[i];
			if(D - a[i] > -eps) T += (D - a[i])/(b[i]*1.0);
		}
		long double ans = D/T;
		cout << fixed << setprecision(11) << ans << endl;
	}
	return 0;
}