#include<iostream>
#include<cstring>
#include<cstdio>
#include<algorithm>
#include<fstream>
using namespace std;
char s[1010];
int h[1010];
int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    long long t, x, ans, cur;
    int cnt, i, j, a[50], b[50];
    int T;
    scanf("%d", &T);
    for(int cas = 1; cas <= T; ++cas)
    {
        scanf("%lld", &x);
        cnt = 0;
        t = x;
        ans = 0;
        while(t)
        {
            a[++cnt] = t % 10;
            t /= 10;
        }
        for(i = 1; i <= cnt; ++i)
        {
            for(j = 1; j <= cnt; ++j)
                b[cnt - j + 1] = a[j];
            t = 0;
            if(b[i] == 0) continue;
            b[i]--;
            for(j = i + 1; j <= cnt; ++j) b[j] = 9;
            cur = b[i];
            for(j = i - 1; j >= 1; --j)
            {
                if(b[j] > cur)
                    b[j] = cur;
                else
                    cur = b[j];
            }
            for(j = 1; j <= cnt; ++j)
                t = t * 10 + b[j];
            ans = max(ans, t);
        }
        for(j = 1; j <= cnt; ++j)
                b[cnt - j + 1] = a[j];
        cur = b[cnt];
        for(i = cnt - 1; i >= 1; --i)
        {
            if(b[i] > cur)
                b[i] = cur;
            else
                cur = b[i];
        }
        t = 0;
        for(j = 1; j <= cnt; ++j) t = t * 10 + b[j];
        ans = max(ans, t);
        printf("Case #%d: ", cas);
        printf("%lld\n", ans);
    }
    return 0;
}
