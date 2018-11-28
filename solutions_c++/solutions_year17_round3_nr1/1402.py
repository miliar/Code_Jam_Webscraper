#include <bits/stdc++.h>
using namespace std;
const int N = 1001000;
const double pi = acos(-1.0);
struct Q
{
    double r, h;
}a[N];

bool cmp(const Q& a, const Q& b)
{
    return a.r < b.r || (a.r == b.r && a.h < b.h);
}

int main()
{
    freopen("a.in", "r", stdin);
    int T, n, K;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas ++)
    {
        scanf("%d%d", &n, &K);
        for (int i = 1; i <= n; i ++)
        {
            scanf("%lf%lf", &a[i].r, &a[i].h);
        }
        sort(a + 1, a + 1 + n, cmp);
        double now = 0, ans = 0;
        set<double> st;
        for (int i = 1; i <= K - 1; i ++)
        {
            st.insert(a[i].r * a[i].h);
            now += a[i].r * a[i].h;
        }
        for (int i = K; i <= n; i ++)
        {
            ans = max(ans, 2 * pi * now + 2 * pi * a[i].r * a[i].h + pi * a[i].r * a[i].r);
            st.insert(a[i].r * a[i].h);
            now += a[i].r * a[i].h;
            now -= *st.begin();
            st.erase(st.begin());
        }
        printf("Case #%d: %.10lf\n", cas, ans);
    }
    return 0;
}
