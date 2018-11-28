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

bool solve()
{
    ll d,n;
    scanf("%lld%lld", &d,&n);
    vector<pair<ll, ll>> v(n);
    for (int i = 0; i < n; ++i) {
        scanf("%lld%lld", &v[i].first, &v[i].second);
    }
    sort(v.begin(), v.end());
    
    double maxT = 0;
    for (int i = 0; i < n; ++i) {
        if (!i || v[i].second < v[i-1].second) {
            maxT = max(maxT, (double)(d - v[i].first) / v[i].second);
        } else if (v[i].second >= v[i-1].second)
            break;
    }
    
    printf("%.7lf\n", d / maxT);
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
