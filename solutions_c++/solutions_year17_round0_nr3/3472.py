#include <iostream>
#include <math.h>

using namespace std;

unsigned long long int solve(unsigned long long int size, unsigned long long int k) {
	unsigned long long left,a,div;
	left = size - k + 1;
	a = pow(2,(unsigned long long) log2(k));
	if (left < a) {
		div = 1;
	} else {
		div = left/a;
		if (left % a != 0) {
			div++;
		}
	}
	return div;
}

int main() {
	int t;
	cin >> t;
	for (int i = 0; i < t; i++) {
		unsigned long long int n,k,ans,mdpt;
		cin >> n >> k;
		ans = solve(n,k);
		cout << "Case #" << i+1 << ": ";
		ans--;
		if (ans % 2 == 0) {
			cout << ans/2 << ' ' << ans/2 << endl;
		} else {
			cout << (ans/2) + 1 << ' ' << ans/2 << endl;
		}
	}
	return 0;
}
