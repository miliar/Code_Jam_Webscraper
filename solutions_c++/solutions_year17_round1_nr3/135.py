#include <bits/stdc++.h>
using namespace std;
const int INF = 1000000000;
int main()
{
    int T;
    scanf("%d", &T);
    int P = 0;
    while (T --)
    {
        P ++;
        int hd, ad, hk, ak, B, D;
        scanf("%d%d%d%d%d%d", &hd, &ad, &hk, &ak, &B, &D);
        int nak = ak, nhd = hd, nct = 0, ans = INF;
        for (int i = 0; i <= ((D == 0)? 0: (ak / D + 1)); ++ i)
        {
            int nnhd = nhd, nad = ad, nnct = nct;
            for (int j = 0; j <= ((B == 0)? 0: (hk - ad / B + 1)); ++ j)
            {
                int nnnhd = nnhd, nhk = hk, nnnct = nnct;
                while (1)
                {
                    if (nhk - nad <= 0) {ans = min(ans, nnnct + 1); break;}
                    if (nnnhd <= nak)
                    {
                        nnnhd = hd;
                        nnnhd -= nak;
                        nnnct ++;
                    }
                    if (nnnhd <= 0) break;
                    nhk -= nad;
                    nnnhd -= nak;
                    nnnct ++;
                    if (nnnhd <= 0) break;
                }

                if (nnhd <= nak)
                {
                    nnhd = hd;
                    nnhd -= nak;
                    nnct ++;
                }
                if (nnhd <= 0) break;
                nad += B;
                nnhd -= nak;
                nnct ++;
                if (nnhd <= 0) break;
            }

            if (nhd <= nak - D)
            {
                nhd = hd;
                nhd -= nak;
                nct ++;
            }
            if (nhd <= 0) break;
            nak -= D;
            nhd -= nak;
            nct ++;
            if (nhd <= 0) break;
        }
        printf("Case #%d: ", P);
        if (ans == INF) puts("IMPOSSIBLE");
        else printf("%d\n", ans);
    }
}
