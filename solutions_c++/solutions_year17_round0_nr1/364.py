#include <bits/stdc++.h>

void flip(std::string& state, int p, int k) {
    for (int i = p; i < p + k; ++ i)
        state[i] = state[i] ^ '+' ^ '-';
}

int main() {
    int T; std::cin >> T;
    for (int t = 1; t <= T; ++ t) {
        std::string state; int k;
        std::cin >> state >> k;
        int ans = 0;
        for (int i = 0; i + k <= (int)state.length(); ++ i) {
            if (state[i] == '-') {
                flip(state, i, k);
                ++ ans;
            }
            //std::cout << state << std::endl;
        }
        bool fail = false;
        for (int i = state.length() - k + 1; i < (int)state.length(); ++ i)
            if (state[i] == '-') {
                fail = true;
                break;
            }
        std::cout << "Case #" << t << ": ";
        if (fail) std::cout << "IMPOSSIBLE" << std::endl;
        else std::cout << ans << std::endl;
    }
}
