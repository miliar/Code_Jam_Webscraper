#include <iostream>
using namespace std;
typedef long long longint;

int log2(longint x) {
	int i = 0;
	while (x/2>=1) {
		i++;
		x /= 2;
	}
	return i;
}

longint pow2(int n) {
	longint x = 1;
	for (int i=0; i<n; i++) {
		x *= 2;
	}
	return x;
}

int main() {
	int t;
	cin >> t;
	for (int tc=1; tc<=t; tc++) {
		longint n, k, l, m;
		cin >> n >> k;
		
		m = pow2(log2(k));
		l = m*2;
		
		longint ma = (n-(k-m))/l;
		longint mi = (n-k)/l;
		cout << "Case #" << tc << ": " << ma << " " << mi << endl;
	}
	return 0;
}