#include <bits/stdc++.h>
using namespace std;
#define LD long double
int n;
LD D;
LD K[1010], V[1010];

LD solve()
{
	scanf("%Lf%d", &D, &n);
	LD mini = 0.0;
	for(int i = 1 ; i <= n ; i++)
	{
		scanf("%Lf%Lf", &K[i], &V[i]);
		mini = max(mini, (D - K[i]) / V[i]);
	}
	return D / mini;
}

int main()
{
	int t;
	scanf("%d", &t);
	for(int i = 1 ; i <= t ; i++)
		printf("Case #%d: %.10Lf\n", i, solve());
}
