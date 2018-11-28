#include <iostream>
#include <vector>
#include <cstdio>

void dothedo() {
    int R, C;
    std::vector<char> g;
    std::vector<int> a;
    std::cin >> R >> C;
    getchar();
    for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++) {
            char c = getchar();
            g.push_back(c);
            if (c != '?') a.push_back(i*C+j);
        }
        getchar();
    }
    if (R > 1) {
        for (auto i : a) {
            int c = i + C;
            while (c < R*C && g[c] == '?') {
                g[c] = g[i];
                c += C;
            }
            c = i - C;
            while (c >= 0 && g[c] == '?') {
                g[c] = g[i];
                c -= C;
            }
        }
    }

    if (C > 1) {
        for (auto i : a) {
            int c = i + 1;
            bool k = true;
            while (c%C > i%C && k) {
                int f = c;
                while (f >= 0 && g[f-1] == g[i]) {
                    if (g[f] != '?') {
                        k = false;
                        break;
                    } else f -= C;
                }
                f = c + C;
                while (f < R*C && g[f-1] == g[i]) {
                    if (g[f] != '?') {
                        k = false;
                        break;
                    } else f += C;
                }
                if (k) {
                    f = c;
                    while (f >= 0 && g[f-1] == g[i]) {
                        g[f] = g[i];
                        f -= C;
                    }
                    f = c + C;
                    while (f < R*C && g[f-1] == g[i]) {
                        g[f] = g[i];
                        f += C;
                    }
                }
                ++c;
            }
            c = i - 1;
            k = true;
            while (c >= 0 && c%C < i%C && k) {
                int f = c;
                while (f >= 0 && g[f+1] == g[i]) {
                    if (g[f] != '?') {
                        k = false;
                        break;
                    } else f -= C;
                }
                f = c + C;
                while (f < R*C && g[f+1] == g[i]) {
                    if (g[f] != '?') {
                        k = false;
                        break;
                    } else f += C;
                }
                if (k) {
                    f = c;
                    while (f >= 0 && g[f+1] == g[i]) {
                        g[f] = g[i];
                        f -= C;
                    }
                    f = c + C;
                    while (f < R*C && g[f+1] == g[i]) {
                        g[f] = g[i];
                        f += C;
                    }
                }
                --c;
            }
        }
    }
    for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++) {
            std::cout << g[i*C+j];
        }
        std::cout << std::endl;
    }
}

int main() {
    int t;
    std::cin >> t;
    for (int i = 0; i < t; i++) {
        std::cout << "Case #" << i+1 << ":" << std::endl;
        dothedo();
    }
    return 0;
}
