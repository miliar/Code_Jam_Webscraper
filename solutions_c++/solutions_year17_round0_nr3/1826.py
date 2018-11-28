#include <bits/stdc++.h>

using namespace std;

long long n, k;
long long p, q;

long long lg(long long k) {
    long long res = 0LL;
    while (k) {
        k >>= 1LL;
        res++;
    }
    return res;
}

void read_input() {
    cin >> n >> k;
}

void solve() {
    long long delay = (k - 1);
    long long step = 1LL << lg(k);
    p = (n - delay - 1LL) / step;
    q = (n - delay + (step >> 1LL) - 1LL) / step;
}

void write_output(int test) {
    cout << "Case #" << test << ": " << q << " " << p << endl;
}

void clear_data() {
    n = k = p = q = 0;
}

int cases;
int main() {
    ios_base::sync_with_stdio(false);

    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);

    cin >> cases;
    for (int test = 1; test <= cases; ++test) {
        read_input();
        solve();
        write_output(test);
        clear_data();
    }
    return 0;
}
