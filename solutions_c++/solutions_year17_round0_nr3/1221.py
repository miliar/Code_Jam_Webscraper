#include <iostream>
#include <cstdio>
typedef long long ll;
using namespace std;

void prt(ll d, ll n, ll x, ll y, ll k)
{
	printf("%lld %lld %lld %lld %lld\n", d, n, x, y, k);
}

ll ans1, ans0;
void work(ll n, ll k)
{
	ll d = 1, cnt0 = 1, cnt1 = 0;
	
	//prt(d, n, cnt0, cnt1, k);
	
	while (k > 0)
	{
		k -= d;
		
		if (n % 2 == 1)
			cnt0 = cnt0 * 2 + cnt1;
		else
			cnt1 = cnt1 * 2 + cnt0;
		
		if (n > 0)
			n = (n - 1) / 2;
		else
			n = (n - 2) / 2;
		
		d *= 2;
		
		//prt(d, n, cnt0, cnt1, k);
		
		/*if (n == 0)
			break;*/
	}
	
	/*if (k > 0)
		ans1 = ans0 = 0;
	else */if (cnt0 >= cnt1)
	{
		if (-k * 2 < cnt0 - cnt1)
			ans1 = ans0 = n;
		else
			ans1 = n + 1, ans0 = n;
	}
	else
	{
		if (-k < cnt0)
			ans1 = n + 1, ans0 = n;
		else
			ans1 = ans0 = n + 1;
	}
}

int main()
{
	/*freopen("qr17cL.in", "r", stdin);
	freopen("qr17cL.out", "w", stdout);*/
	int T;
	ll N, K;
	cin >> T;
	for (int cs = 1; cs <= T; cs++)
	{
		cin >> N >> K;
		
		work(N, K);
		
		printf("Case #%d: %lld %lld\n", cs, ans1, ans0);
	}
	return 0;
}

