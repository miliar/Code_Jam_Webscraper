#include <cstdio>
#include <iostream>

int tab[1000007];

int main() {
    int T;
    scanf("%d", &T);
    for (int w = 1; w <= T; w++) {
        std::string s;
        std::cin >> s;
        for (int i = 0; i < s.length(); i++)
            tab[i] = 0;
        int l = 0;
        int wyn = 0;
        bool impossible = false;
        int K;
        scanf("%d", &K);
        for (int i = 0; i < s.length(); i++) {
            l += tab[i];
            if (s[i] == '-') {
                if (l % 2 == 0) {
                    if (s.length() - i >= K) {
                        l++;
                        wyn++;
                        tab[i + K]--;
                    } else {
                        impossible = true;
                    }
                }
            } else {
                if (l%2 == 1) {
                    if (s.length() - i >= K) {
                        l++;
                        wyn++;
                        tab[i + K]--;
                    } else {
                        impossible = true;
                    }
                }
            }
        }
        if (impossible) {
            printf("Case #%d: IMPOSSIBLE\n", w);
        } else {
            printf("Case #%d: %d\n", w, wyn);
        }
    }
    return 0;
}