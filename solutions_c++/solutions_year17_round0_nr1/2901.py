#include <iostream>
#include <cstdio>
using namespace std;

int T;

void read() {
    cin >> T;
}

void solve() {
    int ok;
    unsigned pow;
    string pancake;
    for (int i = 0; i < T; ++i) {
        cin >> pancake;
        cin >> pow;
        ok = 0;
        for (unsigned j = 0; j < pancake.length() && ok >= 0; ++j) {
            if (pancake[j] == '-') {
                if (j + pow > pancake.length()) {
                    ok = -1;
                } else {
                    for (unsigned k = j; k < j + pow; ++k) {
                        if (pancake[k] == '-') {
                            pancake[k] = '+';
                        } else {
                            pancake[k] = '-';
                        }
                    }
                    ++ok;
                }
            }
        }
        cout << "Case #" << i + 1 << ": ";
        if (ok < 0) {
            cout << "IMPOSSIBLE";
        } else {
            cout << ok;
        }
        cout << endl;
    }
}

int main() {
    freopen("in.in", "r", stdin);
    freopen("out.out", "w", stdout);
    read();
    solve();
    return 0;
}
