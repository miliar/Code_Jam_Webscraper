#include <bits/stdc++.h>
#define ll long long
#define mk make_pair
using namespace std;

const int N = 1e5 + 5;

ll n, k, kk, a, b, d[70];

int main() {
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	int T, cas = 0;
	scanf("%d", &T);
	d[0] = 1;
	for (int i = 1; i < 70; i++) d[i] = d[i - 1] * 2;
	while (T--) {
		cin >> n >> k;
		int j;
		for (int i = 1; i < 70; i++)
			if (d[i] - 1 >= k) {
				j = i;
				break; 
			}
		n -= d[j - 1] - 1;
		k -= d[j - 1] - 1;
		ll s = n / d[j - 1];
		a = n % d[j - 1];
		b = s - a;
		printf("Case #%d: ", ++cas);
		if (k <= a) printf("%lld %lld\n", (s + 1) / 2, s / 2);
		else printf("%lld %lld\n", s / 2, (s - 1) / 2);
	}
}


