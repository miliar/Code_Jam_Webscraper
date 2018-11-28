#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

#define gc getchar
int getint() { unsigned int c; int x = 0; while (((c = gc()) - '0') >= 10) { if (c == '-') return -getint(); if (!~c) exit(0); } do { x = (x << 3) + (x << 1) + (c - '0'); } while (((c = gc()) - '0') < 10); return x; }
int getstr(char *s) { int c, n = 0; while ((c = gc()) <= ' ') { if (!~c) exit(0); } do { s[n++] = c; } while ((c = gc()) > ' ' ); s[n] = 0; return n; }
template<class T> inline bool chmin(T &a, T b) { return a > b ? a = b, 1 : 0; }
template<class T> inline bool chmax(T &a, T b) { return a < b ? a = b, 1 : 0; }
inline ll getll() { unsigned int c; ll x = 0; while (((c = gc()) - '0') >= 10) { if (c == '-') return -getll(); if (!~c) exit(0); } do { x = (x << 3) + (x << 1) + (c - '0'); } while (((c = gc()) - '0') < 10); return x; }

void print_case(int test_case) { printf("Case #%d: ", test_case); }

ll pow10(int e) {
    if (!e) return 1;
    if (e & 1) return 10LL * pow10(e - 1);
    const auto a = pow10(e >> 1);
    return a * a;
}

void solve_case() {
    auto n = getll();
    string s = to_string(n);
    const auto len = s.size();
    for (auto i = 0; i < s.size() - 1; ++i) {
        const ll base = pow10(i);
        const int pos = s.size() - 1 - i;
        while (s[pos] < s[pos - 1]) {
            s = to_string(n - base);
            while (s.size() != len) s = "0" + s;
            for (auto j = pos + 1; j < s.size(); ++j) s[j] = '9';
            n = stoll(s);
        }
    }
    cout << n << endl;
}

int main () {
    int test_count, test_case = getint();
    for (test_count = 0; test_count < test_case; test_count++) {
        print_case(test_count + 1);
        solve_case();
    }
    return 0;
}
