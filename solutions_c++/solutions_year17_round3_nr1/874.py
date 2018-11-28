#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <string>
#include <cstring>
#include <map>
#include <set>
#include <vector>

const int N = 1e3+3;
const int inf = 1e9;

typedef long long ll;

using namespace std;



double getH(ll r, ll h)
{
    return 2 * acos(-1.) * r * h;
}

bool solve()
{
    int n,k;
    scanf("%d%d",&n,&k);
    vector <pair<ll, ll>> p(n);
    long double ans = 0;
    for (auto &r : p)
        scanf("%lld%lld", &r.first, &r.second);
    for (int i = 0; i < n; ++i) {
        long double t = p[i].first * p[i].first * acos(-1.) + getH(p[i].first, p[i].second);
        multiset <ll> s;
        for (int j = 0; j < n; ++j)
            if (j != i && p[j].first <= p[i].first) {
                s.insert(p[j].first * p[j].second);
                if (s.size() > k - 1)
                    s.erase(s.begin());
            }
        if (s.size() != k - 1)
            continue;
        for (auto &p : s) {
            t += 2 * acos(-1.) * p;
        }
        if (ans < t)
            ans = t;
    }
    printf("%.8Lf\n", ans);
    return false;
}

int main()
{
        freopen("input.txt","r", stdin);
        freopen("output.txt", "w", stdout);
    int countTests;
    scanf("%d", &countTests);
    for (int curTest = 1; curTest <= countTests; ++curTest) {
        printf("Case #%d: ", curTest);
        solve();
    }
    
    return 0;
}
