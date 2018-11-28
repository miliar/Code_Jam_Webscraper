#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

bool isSorted(ll n) {
	ll digits[20], k=0;
	while(n) {
		digits[k++] = n%10LL;
		n /= 10LL;
	}
	reverse(digits, digits+k);
	for(int i=1; i<k; ++i)
		if(digits[i] < digits[i-1])	return false;
	return true;
}

ll zz(ll n) {
	ll digits[20], k=0, i, j;
	while(n) {
		digits[k++] = n%10LL;
		n /= 10LL;
	}
	reverse(digits, digits+k);
	for(i=0; i<k-1; ++i) {
		if(digits[i] > digits[i+1]) {
			digits[i]--;
			for(j=i+1; j<k; ++j)
				digits[j] = 9;
			break;
		}
	}
	for(i=0; i<k; ++i)
		n = 10LL*n + (ll)digits[i];
	return n;
}

int main() {
	int i, j, t, tc = 0;
	cin >> t;
	while(t--) {
		tc++;
		cout << "Case #" << tc <<": ";
		ll n;
		cin >> n;
		while(!isSorted(n)) {
			n = zz(n);
		}
		cout << n <<endl;
	}
	return 0;
}