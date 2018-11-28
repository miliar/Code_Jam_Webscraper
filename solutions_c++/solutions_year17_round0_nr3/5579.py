#include <iostream>
#include "stdio.h"
#include <math.h>
#include <algorithm>

using namespace std;
const int maxn = 1010;
int a[maxn] = {0};
int ls[maxn] = {0};
int rs[maxn] = {0};

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t, i, j;
    int n, k;
    cin >> t;
    for (int q = 1; q <= t; ++q) {
        cin >> n >> k;
        for (i = 1; i <= n; ++i) {
            a[i] = 0;
        }
        a[0] = a[n + 1] = 1;
        int pos = -1, mx1 = -1, mx2 = -1;
        for (i = 1; i <= k; ++i) {
            for (j = 1; j <= n; ++j) {
                ls[j] = rs[j] = 0;
                int z = j - 1;
                while (a[z] == 0 && z >= 1) {
                    ++ls[j];
                    --z;
                }
                z = j + 1;
                while (a[z] == 0 && z <= n) {
                    ++rs[j];
                    ++z;
                }
            }
            mx1 = -1;
            mx2 = -1;
            for (j = 1; j <= n; ++j) {
                if (a[j]) {
                    continue;
                }
                int cand1 = min(ls[j], rs[j]);
                int cand2 = max(ls[j], rs[j]);
                if (pos == -1) {
                    pos = j;
                    mx1 = cand1;
                    mx2 = cand2;
                } else {
                    if (cand1 > mx1 || (cand1 == mx1 && cand2 > mx2)) {
                        mx1 = cand1;
                        mx2 = cand2;
                        pos = j;
                    }
                }
            }
            a[pos] = 1;
        }
        cout << "Case #" << q << ": " << mx2 << " " << mx1 << "\n";
    }
    return 0;
}
