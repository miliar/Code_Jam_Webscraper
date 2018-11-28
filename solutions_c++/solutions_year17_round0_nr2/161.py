#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int Cas;

ll C[77];

int main()
{
	for(int i = 0; i < 19; i++) C[i] = !i ? 1 : C[i - 1] * 10 + 1;
	scanf("%d", &Cas);
	for(int TT = 1; TT <= Cas; TT++) {
		printf("Case #%d: ", TT);
		ll n, ans = 0, t = 0;
		scanf("%lld", &n);
		for(int i = 17; i >= 0; i--)
			for(int j = 9; j >= 0; j--)
				if(ans + C[i] * (j - t) <= n) {ans += C[i] * (j - t), t = j; break;}
		printf("%lld\n", ans);
	}
	return 0;
}
