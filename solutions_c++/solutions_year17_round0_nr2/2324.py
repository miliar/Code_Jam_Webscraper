#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;
typedef long long ll;

ll solve(ll x)
{
    vector<int> a;
    while (x > 0) {
        a.push_back(x % 10);
        x /= 10;
    }
    reverse(a.begin(), a.end());
    int n = (int)a.size(), k = 0;
    ll ret = 0;
    for (int i = 1; i < n; i++) {
        if (a[k] < a[i]) k = i;
        else if (a[k] > a[i]) {
            --a[k];
            for (int j = k + 1; j < n; j++)
                a[j] = 9;
            break;
        }
    }
    for (int i = 0; i < n; i++)
        ret = ret * 10 + a[i];
    return ret;
}

int main()
{
    int T;
    scanf("%d", &T);
    for (int tc = 1; tc <= T; tc++) {
        ll n;
        scanf("%lld", &n);
        printf("Case #%d: %lld\n", tc, solve(n));
    }
    return 0;
}
