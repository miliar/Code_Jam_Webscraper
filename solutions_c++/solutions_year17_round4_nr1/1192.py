#include <bits/stdc++.h>

using namespace std;

int num[5];

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("answer.out", "w", stdout);
    int T, cas = 0;
    scanf("%d", &T);
    while(T--)
    {
        int n, p;
        scanf("%d%d", &n, &p);
        for(int i = 0; i < p; ++i) num[i] = 0;
        for(int i = 0; i < n; ++i)
        {
            int x;
            scanf("%d", &x);
            ++num[x % p];
        }
        int ans = 0;
        if(p == 2) ans = num[0] + (num[1] + 1) / 2;
        else if(p == 3)
        {
            ans = num[0];
            int k = min(num[1], num[2]);
            ans += k;
            num[1] -= k, num[2] -= k;
            ans += (num[1] + 2) / 3 + (num[2] + 2) / 3;
        }
        else
        {
            ans = num[0] + num[2] / 2;
            int k = min(num[1], num[3]);
            ans += k;
            num[1] -= k, num[3] -= k;
            num[2] %= 2;
            if(num[2] == 0)
            {
                ans += (num[1] + 3) / 4 + (num[3] + 3) / 4;
            }
            else
            {
                int q = max(num[1], num[3]);
                if(q >= 2) ans += 1 + (q - 2 + 3) / 4;
                else ans += 1;
            }
        }
        printf("Case #%d: ", ++cas);
        printf("%d\n", ans);
    }
    return 0;
}
