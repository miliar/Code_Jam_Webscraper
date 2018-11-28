#include <iostream>
#include <cstdio>
#include <string>

using namespace std;

const int maxn = 22;

typedef long long LL;
LL g[maxn][maxn], f[maxn][maxn];
LL p10[maxn];

int main() {
    freopen("Bl.in", "r", stdin);
    freopen("Blout.txt", "w", stdout);
    int T, ca = 0;
    p10[0] = 1;
    for (int i = 1; i <= 20; ++i) {
        p10[i] = p10[i - 1] * 10;
    }
    cin >> T;
    while (T--) {
        LL num;
        cin >> num;
        int bit = 0;
        while (num != 0) {
            int val = num % 10;
            num /= 10;
            ++bit;
            for (int k = 0; k < 10; ++k) {
                if (bit == 1) {
                    g[bit][k] = k;
                    if (k <= val) f[bit][k] = k; else f[bit][k] = -1;
                } else {
                    //g[bit][k];
                    g[bit][k] = -1;
                    for (int i = k; i < 10; ++i) {
                        if (g[bit - 1][i] != -1) g[bit][k] = max(g[bit][k], g[bit - 1][i] + k * p10[bit - 1]);
                    }
                    //f[bit][k];
                    f[bit][k] = -1;
                    if (k < val) {
                        f[bit][k] = g[bit][k];
                    } else if (k == val) {
                        for (int i = k; i < 10; ++i) {
                            if (f[bit - 1][i] != -1) f[bit][k] = max(f[bit][k], f[bit - 1][i] + k * p10[bit - 1]);
                        }
                    } else if (k > val) {
                        
                    }
                }
            }
        }
        LL ans = 0;
        for (int i = 0; i < 10; ++i) {
            ans = max(ans, f[bit][i]);
        }
        printf("Case #%d: ", ++ca);
        cout << ans << endl;
    }
    return 0;
}