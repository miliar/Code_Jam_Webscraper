#include <bits/stdc++.h>
using namespace std;

typedef long long LL;
typedef pair < int, int > PII;

const int N = 1e3 + 7;

int n, c, m;
int cnt[N], cus[N], tmp[N];

int check(int x)
{
    for(int i = 0; i <= n; i++)
        tmp[i] = cnt[i];
    int ans = 0;
    for(int i = n; i; i--)
    {
        if(tmp[i] > x)
        {
            tmp[i - 1] += tmp[i] - x;
        }
        if(cnt[i] > x)
            ans += cnt[i] - x;
    }
    if(tmp[0] > 0) return -1;
    return ans;
}

int binsearch(int l, int r)
{
    while(l + 1 < r)
    {
        int me = (l + r) / 2;
        check(me) >= 0 ? r = me : l = me;
    }
    return r;
}

int main()
{
    int te; scanf("%d", &te);
    for(int t = 1; t <= te; t++)
    {
        scanf("%d%d%d", &n, &c, &m);
        int mx = 0;
        for(int i = 0; i < m; i++)
        {
            int p, b; scanf("%d%d", &p, &b);
            cnt[p]++, cus[b]++;
            mx = max(cus[b], mx);
        }
        int ans = binsearch(mx - 1, max(mx, m));
        printf("Case #%d: ", t);
        printf("%d %d\n", ans, check(ans));
        for(int i = 1; i <= n; i++)
            cnt[i] = 0;
        for(int i = 1; i <= c; i++)
            cus[i] = 0;
    }
    return 0;
}
