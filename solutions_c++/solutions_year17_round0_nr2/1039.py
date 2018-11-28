#include <bits/stdc++.h>
using namespace std;

typedef long long LL;

LL TEN[19];
int len;

void InitTen() {
	TEN[0] = 1;
	for (int i = 1; i <= 18; i++)
		TEN[i] = TEN[i-1] * 10;
}

LL HighDigit(LL x) {
	return x / TEN[len-1];
}

LL ADD1(LL x, LL y) { 
	return x * TEN[len] + y;
}

LL ADD2(LL x) {
	return x * TEN[len] - 1; 
}

int main() {
	InitTen();
	int T; scanf("%d", &T);
	for (int kk = 1; kk <= T; kk++) {
		LL n, ans; scanf("%lld", &n);
		ans = n % 10;
		n /= 10;
		len = 1;
		while (n != 0) {
			LL cur = n % 10;
			LL high = HighDigit(ans);
			if (cur == 0) {
				
			} else if (cur <= high) {
				ans = ADD1(cur, ans);
			} else {
				ans = ADD2(cur);
			}
			len++;
			n /= 10;
		}
		printf("Case #%d: %lld\n", kk, ans);
	}
	return 0;
}