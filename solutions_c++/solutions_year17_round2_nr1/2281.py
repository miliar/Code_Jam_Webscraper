#include <bits/stdc++.h>

#define pii pair<int, int>
#define pll pair<LL, LL>
#define F first
#define S second
#define B begin()
#define E end()
#define MOD 1000000007
#define itt iterator
#define ritt reverse_iterator
#define LL long long

#define PI (4 * atan(1))

using namespace std;

int t, d, n, p[1005], s[1005];
double mx;

int main()
{
	// freopen("A-large.in", "r", stdin);
	// freopen("A-large.out", "w", stdout);

    scanf("%d", &t);
    for(int z = 1; z <= t; ++z)
    {
    	mx = 0;
    	scanf("%d %d", &d, &n);
    	for(int i = 0; i < n; ++i)
    	{
    		scanf("%d %d", &p[i], &s[i]);
    		mx = max(mx, (double)(d - p[i]) / s[i]);
    	}
    	printf("Case #%d: %lf\n", z, d / mx);
    }
    return 0;
}