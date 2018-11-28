#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <string>
#include <cstring>
#include <map>
#include <set>
#include <vector>

const int N = 1e5+3;
const int inf = 1e9;

typedef long long ll;

using namespace std;

void add(set<pair<ll, ll>> &s, ll val, ll count)
{
    auto it = s.lower_bound({val, - 1});
    if (it != s.end() && val == it->first ) {
        count += it->second;
        s.erase(it);
    }
    s.insert({val, count});
}

bool solve()
{
    ll n,k, i = 0;
    scanf("%lld%lld",&n,&k);
    set <pair<ll, ll>> s;
    s.insert({n, 1});
    while (i < k) {
        auto p = *s.rbegin();
        ll l = (p.first - 1) / 2;
        ll r = p.first - 1 - l;
        if (i + p.second >= k) {
            printf("%lld %lld\n", max(l, r), min(l, r));
            break;
        }
        i += p.second;
        s.erase(p);
        add(s, l, p.second);
        add(s, r, p.second);
    }
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
