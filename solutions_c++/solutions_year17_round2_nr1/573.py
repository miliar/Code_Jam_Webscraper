#include "iostream"
#include "cstdio"
#include "cstdlib"
#include "string.h"
#include "vector"
#include "map"

#define ll long long
#define ull unsigned long long


int main()
{
    freopen("A-large (1).in", "r", stdin);
    freopen("output.txt", "w", stdout);
	int T, cas = 0;
	scanf("%d", &T);
	while(T--)
	{
        cas++;
        int n;
        double D, time = 0.0;
        scanf("%lf%d", &D, &n);
        for (int i = 1; i <= n; i++)
        {
            double K, S;
            scanf("%lf%lf", &K, &S);
            time = std::max(time, (D - K) / S);
        }
        double ans = D / time;
        printf("Case #%d: %.12lf\n", cas, ans);

	}
	return true;
}
