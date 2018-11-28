#include <bits/stdc++.h>

int Hd0, Ad0, Hk0, Ak0, B, D;

int simulate(int cD, int cB) {
    int turn = 0;
    int Hd = Hd0, Ad = Ad0, Hk = Hk0, Ak = Ak0;
    bool lastCure = false;
    while (Hk > 0) {
        bool curCure = false;
        ++ turn;
        if (Hd <= 0) return -1;
        if (Ad >= Hk) {
            break;
        }
        if (Hd <= Ak) {
            if (cD && Hd > std::max(0, Ak - D)) {
                Ak = std::max(0, Ak - D);
                -- cD;
            } else {
                if (lastCure) return -1;
                Hd = Hd0;
                curCure = true;
            }
        }
        else if (cD) {
            Ak = std::max(0, Ak - D);
            -- cD;
        }
        else if (cB) {
            Ad += B;
            -- cB;
        }
        else {
            Hk -= Ad;
        }
        Hd -= Ak;
        lastCure = curCure;
    }
    return turn;
}

int main() {
    int T; std::cin >> T;
    for (int ca = 1; ca <= T; ++ ca) {
        std::cin >> Hd0 >> Ad0 >> Hk0 >> Ak0 >> B >> D;
        std::cout << "Case #" << ca << ": ";
        int ans = -1;
        for (int i = 0; ; ++ i) {
            for (int j = 0; ; ++ j) {
                int tmp = simulate(i, j);
                if (~tmp && (!~ans || tmp < ans)) ans = tmp;
                if (!B || j * B + Ad0 >= Hk0) break;
            }
            if (!D || i * D >= Ak0) break;
        }
        if (~ans) std::cout << ans << std::endl;
        else std::cout << "IMPOSSIBLE" << std::endl;
    }
}
