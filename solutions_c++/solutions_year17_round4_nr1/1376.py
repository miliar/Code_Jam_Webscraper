#include<cstdio>
#include<iostream>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#include<map>
#include<vector>
#include<set>
#include<queue>
using namespace std;

const int maxn = 1010;
int a[maxn];
int cnt[5];

int main()
{
    freopen("A.in","r", stdin);
    freopen("A.out", "w", stdout);
    int T;
    scanf("%d",&T);
    for (int _T = 1; _T <= T; _T++) {
        int n, p;
        scanf("%d%d", &n, &p);
        memset(cnt, 0, sizeof(cnt));
        for (int i = 0; i < n; i++){
            scanf("%d",&a[i]);
            a[i] %= p;
            cnt[a[i]] ++;
        }
        int ans = 0;
        if (p == 2)
        {
            ans = cnt[0];
            ans += (cnt[1] + 1) >> 1;
        }
        if (p == 3)
        {
            ans = cnt[0];
            ans += min(cnt[1], cnt[2]);
            ans += (max(cnt[1], cnt[2]) - min(cnt[1], cnt[2]) + 2) / 3;
        }
        if (p == 4)
        {
            ans = cnt[0];
            ans += min(cnt[1], cnt[3]);
            int u = max(cnt[1], cnt[3]) - min(cnt[1], cnt[3]);
            ans += cnt[2]/2;
            ans += (u + (cnt[2] & 1) * 2 + 3) / 4;
        }
        printf("Case #%d: ", _T);
        printf("%d\n", ans);
    }
    return 0;
}
