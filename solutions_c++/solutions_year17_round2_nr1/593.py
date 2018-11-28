#include <bits/stdc++.h>
using namespace std;

typedef long long LL;
typedef pair < int, int > PII;

int d, n;
vector < PII > v;

int main()
{
    int te; scanf("%d", &te);
    for(int t = 1; t <= te; t++)
    {
        scanf("%d%d", &d, &n);
        long double res = -1, D = d;
        for(int i = 0; i < n; i++)
        {
            long double a, b; scanf("%Lf%Lf", &a, &b);
            if(res == -1) res = (D - a) / b;
            else res = max(res, (D - a) / b);
        }
        printf("Case #%d: %.6Lf\n", t, D / res);
    }
    return 0;
}
