#include <bits/stdc++.h>
using namespace std;
long long tmp, n, satu[50];
int tc;
int main() {
	satu[1] = 1;
	for (int i = 2; i <= 19; ++i)
		satu[i] = satu[i-1]*10LL + 1LL;
	scanf("%d",&tc);
	for (int t = 1; t <= tc; ++t){
		scanf("%lld",&n);
		printf("Case #%d: ", t);
		if (n < 10){
			cout << n << endl;
			continue;
		}
		int len = 0; tmp = n;
		while (tmp > 0){
			tmp /=10;
			len++;
		}
		long long ans = satu[len];
		if (ans > n){
			cout << satu[len-1]*9LL << endl;
			continue;
		}
		int cnt = 1;
		for (int i = len; i >= 1; --i){
			while (cnt < 9 && ans + satu[i] <= n) {ans += satu[i]; cnt++;}
		}
		cout << ans << endl;
	}
}