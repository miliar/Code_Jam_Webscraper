#include<cstdio>
#include<algorithm>
#include<iostream>
#include<cstring>
#include<set>
#include<map>
using namespace std;

const int maxn = 110;

int main() {
    freopen("c.in","r",stdin);
    freopen("c.out","w",stdout);
    int T, cas = 0;
    scanf("%d", &T);
    while (T--) {
        int hd,ad,hk,ak,b,d;
        scanf("%d%d%d%d%d%d", &hd, &ad, &hk, &ak, &b, &d);
        int tb = 0;
        if (b > 0)
        tb = (hk-ad+b-1)/b;
        int td = 0;
        if (d > 0)
        td = (ak+d-1)/d;
        int ans = 100000000;
        for (int x = 0; x <= td; x++)
            for (int y = 0; y <= tb; y++) {
                int tmp = 0;
                int hd_now = hd;
                int ak_now = ak;
                int ad_now = ad;
                int hk_now = hk;
                for (int i = 1; i <= x; i++) {
                    if (hd_now - ak_now+d <= 0) {
                        tmp++;
                        hd_now = hd-ak_now;
                        i--;
                    } else {
                        tmp++;
                        ak_now -= d;
                        hd_now-= ak_now;
                    }
                    if (tmp > 200) {
                        tmp = -1;
                        break;
                    }
                }
                if (tmp == -1) continue;
                
                for (int i = 1; i <= y; i++) {
                    if (hd_now - ak_now <= 0) {
                        tmp++;
                        hd_now = hd-ak_now;
                        i--;
                    } else {
                        tmp++;
                        ad_now += b;
                        hd_now -= ak_now;
                    }
                    if (tmp > 200) {
                        tmp = -1;
                        break;
                    }
                }
                if (tmp == -1) continue;
                while (hk_now > 0) {
                    if (hk_now - ad_now > 0 && hd_now - ak_now <= 0) {
                        tmp++;
                        hd_now = hd-ak_now;
                    } else {
                        tmp++;
                        hk_now -= ad_now;
                        hd_now -= ak_now;
                    }
                    if (tmp > 200) {
                        tmp = -1;
                        break;
                    }
                }
                if (tmp == -1) continue;
                ans = min(ans, tmp);
            }
            printf("Case #%d: ", ++cas);
        if (ans == 100000000) printf("IMPOSSIBLE\n");
        else printf("%d\n", ans);
    }
    return 0;
}
