#include <iostream>
#include "stdio.h"
#include <math.h>
#include <algorithm>

using namespace std;

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    long long n;
    int t, i, j;
    cin >> t;
    string s;
    for (int q = 1; q <= t; ++q) {
        cin >> n;
        int d[22] = {0};
        int cnt = 0;
        while (n != 0) {
            d[cnt++] = n % 10;
            n /= 10;
        }
        for (i = 0; i < cnt / 2; ++i) {
            int tmp = d[i];
            d[i] = d[cnt - i - 1];
            d[cnt - i - 1] = tmp;
        }
        for (i = cnt; i >= 1; --i) {
            d[i] = d[i - 1];
        }
        d[0] = 0;
        i = 1;
        while (i <= cnt) {
            if (d[i] < d[i - 1]) {
                for (j = i; j <= cnt; ++j) {
                    d[j] = 9;
                }
                --d[i - 1];
                i = i - 1;
            } else {
                ++i;
            }
        }
        long long res = 0;
        for (i = 1; i <= cnt; ++i) {
            res = res * 10 + d[i];
        }
        cout << "Case #" << q << ": " << res << "\n";
        //printf("Case #%d: %I64d\n", q, res);
    }
    return 0;
}
