#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int Cas;

int main()
{
	scanf("%d", &Cas);
	for(int TT = 1; TT <= Cas; TT++) {
		printf("Case #%d: ", TT);
		ll n, k, a1, a2, b1, b2;
		scanf("%lld %lld", &n, &k), a1 = n, b1 = n - 1, a2 = 1, b2 = 0;
		while(k > 0) {
			if(a2 >= k) {printf("%lld %lld\n", max(a1 / 2, a1 - 1 - a1 / 2), min(a1 / 2, a1 - 1 - a1 / 2)); break;} else
			if(b2 + a2 >= k) {printf("%lld %lld\n", max(b1 / 2, b1 - 1 - b1 / 2), min(b1 / 2, b1 - 1 - b1 / 2)); break;} else {
				k -= a2 + b2;
				if(a1 % 2 == 1) a2 = a2 * 2 + b2, a1 = b1 / 2, b1 = b1 / 2 - 1;
				else b2 = b2 * 2 + a2, a1 = a1 / 2, b1 = b1 / 2;
			}
		}
	}
	return 0;
}
