#include <bits/stdc++.h>

int main() {
    int T; std::cin >> T;
    for (int t = 1; t <= T; ++ t) {
        std::string n; std::cin >> n;
        std::cout << "Case #" << t << ": ";
        int l = n.length();
        for (int i = 0, le = 0; i < l; ++ i) {
            if (i && n[i] != n[le]) le = i;
            if (i < l - 1 && n[i + 1] < n[i]) {
                -- n[le];
                for (int j = le + 1; j < l; ++ j)
                    n[j] = '9';
                break;
            }
        }
        for (int i = 0; i < l; ++ i) {
            if (n[i] != '0') {
                for (int j = i; j < l; ++ j)
                    putchar(n[j]);
                puts("");
                break;
            }
        }
    }
}
