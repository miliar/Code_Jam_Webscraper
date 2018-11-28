#include <bits/stdc++.h>

using namespace std;

int main() {
	int t;
	long long n,k,kbasemin,kbase,kadd,kpow;
	cin >> t;
	for (int i=1; i<=t; i++) {
		cin >> n >> k;
		kbasemin = 0;
		kbase = 1;
		kadd = 1;
		kpow=0;
		while (kbase<k) {
			kbasemin+=kadd;
			kadd*=2;
			kpow++;
			kbase+=kadd;
		}
		n -= k; //n>=0
		cout << "Case #" << i << ": " << (n+kadd)/(kadd*2) << " " << n/(kadd*2) << endl;
	}
	return 0;
}