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

map<ll, ll> a;

void solve()
{
    ll n, k;
    scanf("%lld%lld", &n, &k);
    k--;
    a.clear();
    a[n] = 1;
    while(true)
    {
        ll x = a.rbegin()->first;
        ll y = a[x];
        if (y == 0)
        {
            a.erase(x);
            continue;
        }
        if (k == 0)
        {
            printf("%lld %lld\n", x / 2, (x - 1) / 2);
            return;
        }
        y = min(y, k);
        k -= y;
        a[x] -= y;
        a[(x - 1) / 2] += y;
        a[x / 2] += y;
    }
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int t;
    scanf("%d", &t);
    for (int i = 0; i < t; i++)
    {
        printf("Case #%d: ", i + 1);
        solve();
    }

    return 0;
}
