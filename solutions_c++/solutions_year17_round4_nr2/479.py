#include <bits/stdc++.h>
using namespace std;
const int N = 10000;
int cnt[N], sum[N];
int T;
int main()
{
    int PPP = 0;
    scanf("%d", &T);
    while (T --)
    {
        PPP ++;
        int n, m, c;
        scanf("%d%d%d", &n, &c, &m);
        memset(cnt, 0, sizeof cnt);
        memset(sum, 0, sizeof sum);
        int ans1 = 0, ans2 = 0;
        for (int i = 1; i <= m; ++ i)
        {
            int a, b;
            scanf("%d%d", &a, &b);
            sum[a] ++;
            cnt[b] ++;
        }
        for (int i = 1; i <= n; ++ i)
            sum[i] += sum[i - 1], ans1 = max(ans1, (sum[i] + (i - 1)) / i);
        for (int i = 1; i <= c; ++ i)
            ans1 = max(ans1, cnt[i]);
        for (int i = 1; i <= n; ++ i)
            ans2 += max(0, sum[i] - sum[i - 1] - ans1);
            cout << "Case #" << PPP << ": ";
        cout << ans1 << " " << ans2 << "\n";
    }
}
