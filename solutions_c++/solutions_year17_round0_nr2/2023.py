#include <bits/stdc++.h>
using namespace std;
#pragma GCC diagnostic ignored "-Wmissing-declarations"

#define FINAL_OUT(x) {cout << (x) << '\n'; exit(0);}

inline bool check(long long x)
{
    int l = 10;
    while (x)
    {
        int nl = x % 10;
        x /= 10;
        if (nl > l)
            return false;
        l = nl;
    }
    return true;
}

void solve(int numtest)
{
    long long n;
    cin >> n;

    long long ans = 0;

    if (check(n))
        ans = n;

    long long def = 1;
    while (def <= n && def > 0)
    {
        long long h = n - 1;
        if (check(h))
            ans = max(ans, h);
        def *= 10;
        n /= def;
        n *= def;
    }

    cout << "Case #" << numtest << ": " << ans << endl;
}

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    ios_base::sync_with_stdio(false);

    //cout << fixed << setprecision(10);

    int t;
    cin >> t;
    for(int i = 1; i <= t; ++i)
        solve(i);
}
