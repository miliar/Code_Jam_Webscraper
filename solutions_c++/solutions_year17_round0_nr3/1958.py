#include <bits/stdc++.h>
using namespace std;

#ifdef LOCAL
#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#define print_var(x) cerr << #x << " = " << x << endl
#define print_array(arr, len) {cerr << #arr << " = "; for (int i = 0; i < len; i++) cerr << arr[i] << " "; cerr << endl;}
#define print_iterable(it) {cerr << #it << " = "; for (const auto &e : it) cerr << e << " "; cerr << endl;}
#else
#define eprintf(...) (void)0
#define print_var(x) (void)0
#define print_array(arr, len) (void)0
#define print_iterable(it) (void)0
#endif

typedef long long ll;

void solve()
{
    ll n, k;
    scanf("%lld%lld", &n, &k);

    k--;
    map<ll, ll> cnt;
    cnt[n] = 1;

    while (true)
    {
        ll x = cnt.rbegin()->first;
        ll c = cnt[x];
        if (k < c)
        {
            printf("%lld %lld\n", x / 2, (x - 1)/ 2);
            break;
        }
        k -= c;
        cnt.erase(x);
        cnt[x / 2] += c;
        cnt[(x - 1) / 2] += c;
    }
}

int main()
{
#ifdef LOCAL
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif

    int t;
    scanf("%d", &t);
    for (int i = 1; i <= t; i++)
    {
        printf("Case #%d: ", i);
        solve();
    }

    eprintf("\n\ntime = %.3lf\n", (double)clock() / CLOCKS_PER_SEC);
}
