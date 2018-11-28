#include <bits/stdc++.h>
#define mp make_pair
#define ft first
#define sd second
#define ue printf("what?\n");
#define pb push_back
#define oo 0x3F3F3F3F
#define OO 0x3F3F3F3F3F3F3F3F
#define EPS 1e-10
#define inf 1000000
#define maxn 200000
#define pi acos(-1)
#define N 100005
#define mdc __gcd

typedef long long ll;

using namespace std;

main()
{
	int t, caso, n, i;
	double d, mx, km, s;
	scanf("%d", &t);
	caso = 1;
	while(t--)
	{
		scanf("%lf%d", &d, &n);
		mx = 0.;
		for(i=0; i<n; i++)
		{
			scanf("%lf%lf", &km, &s);
			mx = max(mx,(d-km)/s);
		}
		printf("Case #%d: %.10lf\n", caso++, (double) d/mx);
	}
}
