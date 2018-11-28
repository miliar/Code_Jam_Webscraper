#include <bits/stdc++.h>
using namespace std;

const int INF = 1000000000, MAXQ = 100;

int calc(int H0, int Hd, int Ad, int Hk, int Ak, int B, int D, int NB, int ND)
{
    int cur = 0;
    while (true) {
        if (cur > 1000) return INF;

        if (Hd <= 0) return INF;
        ++cur;

        if (ND > 0) {
            if (Hd-max(Ak-D, 0) <= 0) { Hd = H0-Ak; continue; }
            --ND; Ak = max(Ak-D, 0); Hd -= Ak;
            continue;
        }

        if (Hk-Ad <= 0) return cur;
        if (Hd-Ak <= 0) { Hd = H0-Ak; continue; }

        if (NB > 0) {
            --NB; Ad += B; Hd -= Ak;
            continue;
        }

        Hk -= Ad; Hd -= Ak;
    }
}

int main()
{
    int T; scanf("%d", &T);
    for (int t = 0; t < T; ++t) {
        int Hd, Ad, Hk, Ak, B, D;
        scanf("%d%d%d%d%d%d", &Hd, &Ad, &Hk, &Ak, &B, &D);

        int answer = INF;

        for (int ND = 0; ND <= MAXQ; ++ND)
            for (int NB = 0; NB <= MAXQ; ++NB) {
                int cur = calc(Hd, Hd, Ad, Hk, Ak, B, D, NB, ND);
                answer = min(answer, cur);
            }

        if (answer == INF)
            printf("Case #%d: IMPOSSIBLE\n", t+1);
        else
            printf("Case #%d: %d\n", t+1, answer);
    }

    return 0;
}
