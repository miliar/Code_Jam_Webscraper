#include <iostream>
#include "stdio.h"
#include <math.h>
#include <algorithm>

using namespace std;

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int n, m, i, j, t, k, x;
    cin >> t;
    string s;
    for (int q = 1; q <= t; ++q) {
        cin >> s >> k;
        int res = 0;
        int bad = 0;
        int sz = s.length();
        for (int i = 0; i < sz; ++i) {
            if (s[i] == '-' && i + k <= sz) {
                ++res;
                for (int j = i; j < i + k; ++j) {
                    if (s[j] == '+') {
                        s[j] = '-';
                    } else {
                        s[j] = '+';
                    }
                }
            }
        }
        for (int i = 0; i < sz; ++i) {
            if (s[i] == '-') {
                bad = 1;
                break;
            }
        }
        if (!bad) {
            printf("Case #%d: %d\n", q, res);
        } else {
            printf("Case #%d: IMPOSSIBLE\n", q, res);
        }
    }
    return 0;
}
