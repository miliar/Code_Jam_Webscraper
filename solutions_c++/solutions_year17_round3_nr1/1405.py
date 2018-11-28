// GCJ 2017R1C A
#include <bits/stdc++.h>

using namespace std;
using ll = long long;

#define gc getchar
int getint() { unsigned int c; int x = 0; while (((c = gc()) - '0') >= 10) { if (c == '-') return -getint(); if (!~c) exit(0); } do { x = (x << 3) + (x << 1) + (c - '0'); } while (((c = gc()) - '0') < 10); return x; }
int getstr(char *s) { int c, n = 0; while ((c = gc()) <= ' ') { if (!~c) exit(0); } do { s[n++] = c; } while ((c = gc()) > ' ' ); s[n] = 0; return n; }
template<class T> bool chmin(T &a, T b) { return a > b ? a = b, 1 : 0; }
template<class T> bool chmax(T &a, T b) { return a < b ? a = b, 1 : 0; }

void print_case(int test_case) { printf("Case #%d: ", test_case); }

double radius[1 << 10];
double heights[1 << 10];

void solve_case() {
    int n = getint();
    int k = getint();
    for (auto i = 0; i < n; ++i) {
        radius[i] = getint();
        heights[i] = getint();
    }
    const double pi = acos(-1.0);
    double res = 0.0;
    for (auto i = 0; i < n; ++i) {
        vector<int> can_use;
        for (auto j = 0; j < n; ++j) if (i != j) {
            if (radius[j] <= radius[i]) {
                can_use.emplace_back(j);
            }
        }
        double tmp = pi * radius[i] * radius[i] + 2.0 * pi * radius[i] * heights[i];
        if (k == 1) {
            chmax(res, tmp);
            continue;
        }
        if (can_use.size() < k - 1) continue;
        sort(can_use.begin(), can_use.end(), [&](int a, int b) {
            auto p = 2.0 * pi * heights[a] * radius[a];
            auto q = 2.0 * pi * heights[b] * radius[b];
            return p > q;
        });
        for (auto j = 0; j < k - 1; ++j) {
            const auto t = can_use[j];
            tmp += 2.0 * pi * heights[t] * radius[t];
        }
        chmax(res, tmp);
    }
    printf("%.10f\n", res);
    return;
}

int main () {
    const auto test_case = getint();
    for (auto test_count = 0; test_count < test_case; test_count++) {
        print_case(test_count + 1);
        solve_case();
    }
    return 0;
}
