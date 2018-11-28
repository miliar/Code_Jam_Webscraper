#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>

using namespace std;

typedef long long ll;
typedef pair<ll, ll> pll;

ll a[10], b[10];
pll p[10];

void solve(ll n, ll k)
{
    a[0] = 1;
    b[0] = n;
    int cnt = 1;
    while(true)
    {
        ll sum = 0;
        for(int i = 0; i < cnt; ++i) sum += a[i];
        if(k > sum)
        {
            int m = 0;
            for(int i = 0; i < cnt; ++i)
            {
                p[m++] = pll((b[i] - 1) / 2, a[i]);
                p[m++] = pll(b[i] / 2, a[i]);
            }
            sort(p, p + m, greater<pll>());
            cnt = 0;
            for(int i = 0; i < m; ++i)
            {
                if(p[i].first != 0)
                {
                    if(cnt == 0 || p[i].first != p[i - 1].first)
                    {
                        b[cnt] = p[i].first;
                        a[cnt++] = p[i].second;
                    }
                    else
                    {
                        a[cnt - 1] += p[i].second;
                    }
                }
            }
            k -= sum;
        }
        else
        {
            sum = 0;
            for(int i = 0; i < cnt; ++i)
            {
                sum += a[i];
                if(sum >= k)
                {
                    printf("%lld %lld\n", b[i] / 2, (b[i] - 1) / 2);
                    return;
                }
            }
        }
    }
}

int main()
{
    freopen("C-large.in", "r", stdin);
    freopen("answer.out", "w", stdout);
    int T, cas = 0;
    scanf("%d", &T);
    while(T--)
    {
        ll n, k;
        scanf("%lld%lld", &n, &k);
        printf("Case #%d: ", ++cas);
        solve(n, k);
    }
    return 0;
}
