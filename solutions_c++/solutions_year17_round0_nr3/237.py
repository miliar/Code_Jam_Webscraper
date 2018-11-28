#include <bits/stdc++.h>
using namespace std;

int main() {
	int tc;
	scanf("%d", &tc);
	for (int i=1; i<=tc; i++) {
		long long n,k;
		scanf("%lld%lld", &n, &k);
		long long mx,mn;
		while (k>0) {
			k-=1;
			n-=1;
			if (k==0) break;
			if (k%2==1) {
				k=(k+1)/2;
				n=(n+1)/2;
			}
			else n=n/2, k=k/2;
		}
		mx=(n+1)/2, mn=n/2;
		printf("Case #%d: %lld %lld\n", i, mx, mn);
	}
}
