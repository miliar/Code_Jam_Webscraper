#include <cstdio>
#include <algorithm>
using namespace std;
typedef long double LD;
#define N 50 + 5
#define eps 1e-9

int Case, n, k;
LD x, sum, P[N];

double Get_LD()
{
	double t;
	scanf("%lf", &t);
	return t;
}

bool Check(LD t)
{
	LD sum = 0.0;
	for (int i = 1; i <= n; i ++)
		sum += max((LD) 0.0, t - P[i]);
	return sum <= x;
}

void Brute()
{
	LD l = 0.0, r = 1.0;
	while (l + eps < r)
	{
		LD mid = (l + r) / 2;
		if (Check(mid)) l = mid;
		else r = mid;
	}
	for (int i = 1; i <= n; i ++)
		P[i] = max(P[i], l);
}

int main()
{
	scanf("%d", &Case);
	for (int Test = 1; Test <= Case; Test ++)
	{
		scanf("%d%d", &n, &k);
		x = Get_LD();
		for (int i = 1; i <= n; i ++)
			P[i] = Get_LD();
		if (n == k) Brute();
		LD sum = 1.0;
		for (int i = 1; i <= n; i ++)
			sum *= P[i];
		printf("Case #%d: %.7f\n", Test, (double) sum);
	}
	return 0;
}
