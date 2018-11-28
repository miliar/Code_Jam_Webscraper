#include <bits/stdc++.h>

using namespace std;
using ll = long long;

#define gc getchar
int getint() { unsigned int c; int x = 0; while (((c = gc()) - '0') >= 10) { if (c == '-') return -getint(); if (!~c) exit(0); } do { x = (x << 3) + (x << 1) + (c - '0'); } while (((c = gc()) - '0') < 10); return x; }
int getstr(char *s) { int c, n = 0; while ((c = gc()) <= ' ') { if (!~c) exit(0); } do { s[n++] = c; } while ((c = gc()) > ' ' ); s[n] = 0; return n; }
template<class T> bool chmin(T &a, T b) { return a > b ? a = b, 1 : 0; }
template<class T> bool chmax(T &a, T b) { return a < b ? a = b, 1 : 0; }

void print_case(int test_case) { printf("Case #%d: ", test_case); }

int height, width;
char in[30][30];

void solve_case() {

    height = getint();
    width  = getint();
    for (auto i = 0; i < height; ++i) getstr(in[i]);


    for (auto i = 0; i < height; ++i) {
        for (auto j = 0; j < width; ++j) {
            int c = in[i][j];
            if (c != '?') {
                for (auto ii = i - 1; ~ii; --ii) {
                    if (in[ii][j] != '?') break;
                    in[ii][j] = c;
                }
                for (auto ii = i + 1; ii < height; ++ii) {
                    if (in[ii][j] != '?') break;
                    in[ii][j] = c;
                }
            }
        }
    }

    for (auto i = 0; i < height; ++i) {
        for (auto j = 0; j < width; ++j) {
            int c = in[i][j];
            if (c == '?') continue;
            for (auto jj = j + 1; jj < width; ++jj) {
                if (in[i][jj] == '?') {
                    in[i][jj] = c;
                } else break;
            }

        }
    }

    for (auto i = 0; i < height; ++i) {
        for (auto j = 0; j < width; ++j) {
            int c = in[i][j];
            if (c == '?') continue;
            for (auto jj = j - 1; ~jj; --jj) {
                if (in[i][jj] == '?') {
                    in[i][jj] = c;
                } else break;
            }
        }
    }

    puts("");
    for (auto i = 0; i < height; ++i) {
        for (auto j = 0; j < width; ++j) {
            putchar(in[i][j]);
        }
        puts("");
    }
    puts("");


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
