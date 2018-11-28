#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <vector>

using namespace std;

long long f[2][11][22];

long long cnt(long long n) {
    vector<int> digits;
    long long pn = n;
    while (pn > 0LL) {
        digits.push_back((int)(pn % 10LL));
        pn /= 10LL;
    }
    reverse(digits.begin(), digits.end());
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 11; j++) {
            for (int u = 0; u < 22; u++) {
                f[i][j][u] = 0LL;
            }
        }
    }
    f[1][0][0] = 1LL;
    int len = (int)digits.size();
    for (int i = 0; i < len; i++) {
        for (int lst = 0; lst < 10; lst++) {
            for (int newC = lst; newC < 10; newC++) {
                if (newC < digits[i]) {
                    f[0][newC][i + 1] += f[0][lst][i];
                    f[0][newC][i + 1] += f[1][lst][i];
                } else if (newC == digits[i]) {
                    f[0][newC][i + 1] += f[0][lst][i];
                    f[1][newC][i + 1] += f[1][lst][i];
                } else if (newC > digits[i]) {
                    f[0][newC][i + 1] += f[0][lst][i];
                }
            }
        }
    }
    long long ans = 0LL;
    for (int i = 0; i < 10; i++) {
        ans += f[0][i][len];
        ans += f[1][i][len];
    }
    return ans;
}

void solve() {
    long long n;
    cin >> n;
    if (n == 1) {
        cout << 1 << endl;
        return;
    }
    long long cur_cnt = cnt(n);
    long long le = 1LL;
    long long ri = n;
    while (ri - le > 1LL) {
        long long mid = (le + ri) / 2LL;
        if (cnt(mid) < cur_cnt) {
            le = mid;
        } else {
            ri = mid;
        }
    }
    cout << le + 1 << endl;
}

int main() {
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int tc;
    cin >> tc;
    for (int i = 1; i <= tc; i++) {
        cout << "Case #" << i << ": ";
        solve();
    }
    return 0;
}