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

ll sc()
{
    int x,y;
    scanf("%d.%d", &x,&y);
    return x * 10000 + y;
}

bool solve()
{
    int n,k;
    scanf("%d%d", &n, &k);
    ll u = sc(), x;
    multiset<ll> s;
    for (int i = 0; i < n; ++i) {
        s.insert(sc());
    }
    while (u) {
        x = *s.begin();
        s.erase(s.begin());
        x++;
        s.insert(x);
        u--;
    }
    double ans = 1.;
    for (auto p : s)
        ans *= p / 10000.;
    printf("%.7lf\n", ans);
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
