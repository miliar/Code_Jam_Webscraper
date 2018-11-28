#include <bits/stdc++.h>
using namespace std;
int w[105];
int cnt[5];
int main()
{
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    int c = 1, cas;
    scanf("%d", &cas);
    while(cas--)
    {
        int n, p;
        scanf("%d %d", &n ,&p);
        for(int i = 0; i < n; i++)
            scanf("%d", &w[i]);
        memset(cnt, 0, sizeof(cnt));
        for(int i = 0; i < n; i++)
            cnt[w[i] % p]++;
        int ans = 0;
        if(p == 2)
        {
            ans = cnt[0] + (cnt[1] + 1) / 2;
        }
        else if(p == 3)
        {
            ans += cnt[0];
            int mn12 = min(cnt[1], cnt[2]);
            ans += mn12;
            cnt[1] -= mn12;
            cnt[2] -= mn12;
            ans += (cnt[1] + 2) / 3;
            ans += (cnt[2] + 2) / 3;
        }
        else if(p == 4)
        {
            ans += cnt[0];
            int mn13 = min(cnt[1], cnt[3]);
            ans += mn13;
            cnt[1] -= mn13;
            cnt[3] -= mn13;
            ans += cnt[2] / 2;
            cnt[2] = cnt[2] % 2;
            if(cnt[2] == 0)
            {
                ans += (cnt[1] + 3) / 4;
                ans += (cnt[3] + 3) / 4;
            }
            if(cnt[2] != 0)
            {
                if(cnt[1] >= 2 || cnt[3] >= 2)
                {
                    ans += 1;
                    cnt[1] = max(0, cnt[1] - 2);
                    cnt[3] = max(0, cnt[3] - 2);
                    ans += (cnt[1] + 3) / 4;
                    ans += (cnt[3] + 3) / 4;
                }
                else
                {
                    ans += 1;
                }
            }
        }
        printf("Case #%d: %d\n", c++, ans);
    }
    return 0;
}
