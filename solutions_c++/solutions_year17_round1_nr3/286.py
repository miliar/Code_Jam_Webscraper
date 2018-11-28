#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
using namespace std;

/* #define debug printf */
#define debug(...)
typedef long long ll;

int gHd, gAd, gHk, gAk, B, D;

#define MAX_INT 2147483647

int simulate(int nd, int nb) {
    int cost = 0;
    int Hd = gHd, Ad = gAd, Hk = gHk, Ak = gAk;
    for (int i = 0; i < nd; i++) {
        if (Hd - (Ak-D) <= 0) {
            Hd = gHd, cost += 1, Hd -= Ak;
            if (Hd <= 0) return MAX_INT;
        }
        Ak -= D, cost += 1, Hd -= Ak;
        if (Hd <= 0) return MAX_INT;
    }
    for (int i = 0; i < nb; i++) {
        if (Hd - Ak <= 0) {
            Hd = gHd, cost += 1, Hd -= Ak;
            if (Hd <= 0) return MAX_INT;
        }
        Ad += B, cost += 1, Hd -= Ak;
        if (Hd <= 0) return MAX_INT;
    }
    /* debug("----\n"); */
    while (true) {
        if (Hd - Ak <= 0 && Hk - Ad > 0) {
            /* debug("Heal\n"); */
            Hd = gHd, cost += 1, Hd -= Ak;
            if (Hd <= 0) return MAX_INT;
        }
        /* debug("Attack\n"); */
        Hk -= Ad, cost += 1;
        if (Hk <= 0) break;
        Hd -= Ak;
        if (Hd <= 0) return MAX_INT;
    }
    /* debug("WIN\n"); */
    return cost;
}

void solve(int T) {
    scanf("%d%d%d%d%d%d", &gHd, &gAd, &gHk, &gAk, &B, &D);
    int best = MAX_INT;
    for (int nd = 0; nd <= 100; nd++) {
        for (int nb = 0; nb <= 100; nb++) {
            int cost = simulate(nd, nb);
            if (cost < best) {
                best = cost;
                debug("Best: (%d steps) nd = %d, nb = %d\n", cost, nd, nb);
            }
        }
    }
    if (best == MAX_INT)
        printf("Case #%d: IMPOSSIBLE\n", T);
    else
        printf("Case #%d: %d\n", T, best);
}

int main() {
    int T; scanf("%d", &T);
    for (int t = 1; t <= T; t++)
        solve(t);
    return 0;
}
