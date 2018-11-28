#include <cstdio>
#include <cstring>

int casei, cases, now, last;
long long ans1, ans2, m;
long long cnts[2][2];
long long ns[2][2];

int main() {
	scanf("%d", &cases);
	for (casei = 1; casei <= cases; ++casei) {
		scanf("%lld%lld", ns[0], &m);
		ns[0][1] = 0LL;
		cnts[0][0] = 1LL;
		cnts[0][1] = 0LL;
		now = 0;
		last = 1;
		//printf("ns %lld %lld; m %lld\n", ns[now][0], ns[now][1], m);
		
		while (m > cnts[now][0] + cnts[now][1]) {
			m -= cnts[now][0] + cnts[now][1];
			
			now ^= 1; last ^= 1;
			
			if (cnts[last][1] == 0) {
				if ((ns[last][0] & 1LL) == 0LL) {
					ns[now][0] = ns[last][0] >> 1LL;
					ns[now][1] = ns[now][0] - 1LL;
					cnts[now][0] = cnts[last][0];
					cnts[now][1] = cnts[last][0];
				}
				else {
					ns[now][0] = ns[last][0] >> 1LL;
					cnts[now][0] = cnts[last][0] << 1LL;
					cnts[now][1] = 0LL;
				}
			}
			else {
				if ((ns[last][0] & 1LL) == 0LL) {
					// ns[last][0] is even
					ns[now][0] = ns[last][0] >> 1LL;
					ns[now][1] = ns[now][0] - 1LL;
					cnts[now][0] = cnts[last][0];
					cnts[now][1] = cnts[last][0];
					// ns[last][1] == ns[last][0] - 1 is odd
					cnts[now][1] += cnts[last][1] << 1LL;
				}
				else {
					// ns[last][0] is odd
					ns[now][0] = ns[last][0] >> 1LL;
					ns[now][1] = ns[now][0] - 1LL;
					cnts[now][0] = cnts[last][0] << 1LL;
					// ns[last][1] == ns[last][0] - 1 is even
					cnts[now][0] += cnts[last][1];
					cnts[now][1] = cnts[last][1];
				}
			}
		}
		
		long long num = 0;
		if (m <= cnts[now][0]) {
			num = ns[now][0];
		}
		else {
			num = ns[now][1];
		}
		
		ans1 = num >> 1LL; ans2 = ans1;
		if ((num & 1LL) == 0LL) {
			--ans2;
		}
		
		//printf("ns %lld %lld\n", ns[now][0], ns[now][1]);
		//printf("num %lld\n", num);
		printf("Case #%d: %lld %lld\n", casei, ans1, ans2);
	}
	return 0;
}
