#include <bits/stdc++.h>


using namespace std;
#define FOR(i, n) for (int i=0; i<(n); i++)
#define ll long long

void konec(ll a)
{
	printf("%lld %lld\n", a / 2, (a - 1) / 2);
}

void vyres(void)
{
	ll n, k;
	scanf("%lld %lld", &n, &k);
	ll a = n, ca = 1, cb = 0;
	while (true){
		// b = a - 1
		k -= ca;
		if (k <= 0){
			konec(a);
			return;
		}

		k -= cb;
		if (k <= 0){
			konec(a - 1);
			return;
		}

		ll da, db;
		ll na = a / 2;
		if (a % 2)
			da = 2 * ca + cb, db = cb;
		else
			da = ca, db = ca + 2 * cb;

		ca = da, cb = db;
		a = na;
	}
}

int main(void)
{
	int t;
	scanf("%d", &t);
	FOR(i, t){
		printf("Case #%d: ", i + 1);
		vyres();
	}
}
