#include <bits/stdc++.h>
using namespace std;
typedef long long LL;
const int N=1e4+5;
const double eps=1e-3;
const int INF=1e9;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A.out", "w", stdout);
    int t, ca=1;
    scanf("%d", &t);
    while(t--)
    {
        printf("Case #%d: ", ca++);
        int n, d;
        scanf("%d%d", &d, &n);
        double ans=0;
        for(int i=0;i<n;i++)
        {
            int k, s;
            scanf("%d%d", &k, &s);
            ans=max(ans, (d-k)/(s*1.0));
        }
        printf("%.6f\n", d/(ans*1.0));
    }
    return 0;
}
