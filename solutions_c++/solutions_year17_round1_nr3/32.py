#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <cmath>
#include <ctime>
#include <string>
#include <cstring>
#include <complex>
using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
#define mp make_pair

ll Hd, Ad, Hk, Ak, B, D;

void solve()
{
    scanf("%lld%lld%lld%lld%lld%lld", &Hd, &Ad, &Hk, &Ak, &B, &D);
    ll toAtt = (Hk + Ad - 1) / Ad;
    if (B != 0)
    {
        for (ll i = 1; i <= toAtt; i++)
            toAtt = min(toAtt, i + (Hk + Ad + B * i - 1) / (Ad + B * i));
    }
    if (toAtt == 1)
    {
        printf("1\n");
        return;
    }
    if (toAtt == 2 && Hd > Ak)
    {
        printf("2\n");
        return;
    }
    if (max(0LL, Ak - D) + max(0LL, Ak - 2 * D) >= Hd)
    {
        printf("IMPOSSIBLE\n");
        return;
    }
    ll ans = (ll)1e11;
    ll H = Hd;
    ll curMoves = 0;
    while(curMoves + toAtt < ans)
    {
        if (toAtt == 2)
        {
            if (H > Ak)
                ans = min(ans, curMoves + 2);
            if (Hd > 2 * Ak)
                ans = min(ans, curMoves + 3);
        }
        if (Hd > 2 * Ak)
        {
            if (Ak == 0)
                ans = min(ans, curMoves + toAtt);
            else
            {
                ll curRes = curMoves + toAtt;
                ll z = (H - 1) / Ak;
                if (z >= toAtt)
                {
                    ans = min(ans, curRes);
                }
                else
                {
                    curRes++;
                    ll leftAtt = toAtt - z;
                    z = (Hd - Ak - 1) / Ak;
                    curRes += (leftAtt - 2) / z;
                    ans = min(ans, curRes);
                }
            }
        }
        ll nA = max(0LL, Ak - D);
        if (H <= nA)
        {
            curMoves++;
            H = Hd - Ak;
        }
        curMoves++;
        Ak = nA;
        H -= Ak;
    }
    printf("%lld\n", ans);
    return;
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int t;
    scanf("%d", &t);
    for (int i = 1; i <= t; i++)
    {
        cerr << i << endl;
        printf("Case #%d: ", i);
        solve();
    }

    return 0;
}
