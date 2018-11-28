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
const int lim = 24 * 60;

typedef long long ll;

using namespace std;

bool contain(int l, int r, int a, int b)
{
    return l <= a && b <= r;
}


bool intersect(int l, int r, int a, int b)
{
    return l <= a && a < r || l < b && b <= r;
}

bool solve()
{
    int n,m;
    scanf("%d%d",&n,&m);
    vector<int> v(24 * 60, 0);
    vector<pair<int, int>> p(n+m);
    for (int i = 0; i < n + m; ++i) {
        scanf("%d%d", &p[i].first, &p[i].second);
    }
    
    for (int i = 0; i < lim - 720; ++i) {
        bool f = false;
        
        for (int j = 0; j < n; ++j)
            if (!contain(i, i + 720, p[j].first, p[j].second))
                f = true;
        
        for (int j = n; j < p.size(); ++j)
            if (intersect(i, (i + 720), p[j].first, p[j].second)) {
                f = true;
            }
        if (!f) {
            puts("2");
            return false;
        }
    }
    
    if (n && m)
        swap(p[0], p[1]);
    swap(n,m);
    
    for (int i = 0; i < lim - 720; ++i) {
        bool f = false;
        
        for (int j = 0; j < n; ++j)
            if (!contain(i, i + 720, p[j].first, p[j].second))
                f = true;
        
        for (int j = n; j < p.size(); ++j)
            if (intersect(i, (i + 720), p[j].first, p[j].second)) {
                f = true;
            }
        if (!f) {
            puts("2");
            return false;
        }
    }

    puts("4");
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
