// GCJ2017 Round 1B A
#include <bits/stdc++.h>

using namespace std;
using ll = long long;

#define gc getchar
int getint() { unsigned int c; int x = 0; while (((c = gc()) - '0') >= 10) { if (c == '-') return -getint(); if (!~c) exit(0); } do { x = (x << 3) + (x << 1) + (c - '0'); } while (((c = gc()) - '0') < 10); return x; }
template<class T> bool chmin(T &a, T b) { return a > b ? a = b, 1 : 0; }
template<class T> bool chmax(T &a, T b) { return a < b ? a = b, 1 : 0; }

void print_case(int test_case) { printf("Case #%d: ", test_case); }

double poss[1 << 10];
double vels[1 << 10];

double change_at[1 << 10];
const double inf = 1e30;

void solve_case() {
    double d = getint();
    int n = getint();
    for (auto i = 0; i < n; ++i) {
        change_at[i] = inf;
        poss[i] = getint();
        vels[i] = getint();
    }
    for (auto i = 1; i < n; ++i) {
        for (auto j = 0; j < i; ++j) {
            double v2 = vels[i];
            double v1 = vels[i];
            if (v2 <= v1) continue;
            double pos2 = poss[i];
            double pos1 = poss[i];
            double tm = (pos1 - pos2) / (v2 - v1);
            chmin(change_at[i], tm);
        }
    }
    double lt = 0.0, rg = 1e30;
    for (auto step = 0; step < 300; ++step) {
        double v = (lt + rg) / 2.0;
        int ok = 1;
        for (auto i = 0; i < n; ++i) {
            double v1 = vels[i];
            double v2 = v;
            if (v2 > v1) {
                double t = poss[i] / (v2 - v1);
                if (t >= change_at[i]) continue;
                double p = v2 * t;
                if (p <= d) ok = 0;
            }
        }
        if (ok) {
            lt = v;
        } else {
            rg = v;
        }
    }
    printf("%.10f\n", (lt + rg) / 2.0);
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
