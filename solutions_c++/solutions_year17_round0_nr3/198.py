#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

const int MAXL = 1E3 + 10;

char s[MAXL];

int main(){
	int cas;
	scanf("%d", &cas);
	for (int casi = 1; casi <= cas; ++casi){
		printf("Case #%d: ", casi);

		ll n, m;
		scanf("%lld%lld", &n, &m);
		ll cnt[2] = {1, 0};
		for (; m > cnt[0] + cnt[1]; ){
			m -= cnt[0] + cnt[1];

			ll t[2] = {cnt[0], cnt[1]};
			if (n & 1){
				cnt[0] = t[0] * 2 + t[1];
				cnt[1] = t[1];
			}
			else{
				cnt[0] = t[0];
				cnt[1] = t[0] + t[1] * 2;
			}
			n = n - 1 >> 1;
		}
		ll ans = n + (m <= cnt[1]);
		printf("%lld %lld\n", ans >> 1, ans - 1 >> 1);
	}
	return 0;
}
