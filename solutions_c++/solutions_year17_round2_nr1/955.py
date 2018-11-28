#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>

using namespace std;

typedef pair<int, int> pii;

const int maxn = 1000 + 5;
const double INF = 1e15;
const double eps = 1e-8;


pii pp[maxn];
bool used[maxn];
double p1[maxn], s1[maxn];

int dcmp(double x)
{
    if(fabs(x) < eps) return 0;
    return x > 0 ? 1 : -1;
}

bool check(double m, int n, int d)
{
    p1[0] = 0, s1[0] = m;
    used[0] = false;
    for(int i = 1; i <= n; ++i)
    {
        p1[i] = pp[i].first;
        s1[i] = pp[i].second;
        used[i] = false;
    }
    while(true)
    {
        int id = -1;
        double t = INF;
        for(int i = 0; i < n; ++i)
        {
            if(used[i] || dcmp(s1[i + 1] - s1[i]) >= 0) continue;
            double tmp = (p1[i + 1] - p1[i]) / (s1[i] - s1[i + 1]);
            if(dcmp(t - tmp) > 0)
            {
                t = tmp;
                id = i;
            }
        }
        if(id == -1) return true;
        for(int i = 0; i <= n; ++i)
        {
            p1[i] += s1[i] * t;
        }
        if(dcmp(p1[0] - d) >= 0) return true;
        for(int i = n; i > 0; --i)
        {
            if(dcmp(p1[i - 1] - p1[i]) == 0)
            {
                used[i - 1] = true;
                s1[i - 1] = s1[i];
            }
        }
        if(dcmp(p1[0] - p1[1]) == 0) break;
    }
    return dcmp(p1[0] - d) >= 0;
}

int main()
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("ans.out", "w", stdout);
    int T, cas = 0;
    scanf("%d", &T);
    while(T--)
    {
        int d, n;
        scanf("%d%d", &d, &n);
        for(int i = 1; i <= n; ++i) scanf("%d%d", &pp[i].first, &pp[i].second);
        sort(pp + 1, pp + n + 1);
        double l = 0, r = INF;
        for(int i = 0; i < 100; ++i)
        {
            double m = (l + r) / 2;
            if(check(m, n, d)) l = m;
            else r = m;
        }
        printf("Case #%d: ", ++cas);
        printf("%.10f\n", l);
    }
    return 0;
}
