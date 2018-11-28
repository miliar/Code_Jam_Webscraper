#include <bits/stdc++.h>

using namespace std;

typedef long long LL;

const int N = 5555;
const double eps = 1e-9;

int T, cas, a[55], b[55][55], n, m, p[55];

int Calc() {
    int tot = 0;
    while (1) {
        int mxi = -1, mni = 10000000;
        for (int i = 1; i <= n; i ++) {
            int li = ceil(b[i][p[i]] / 1.1 - eps);
            int ri = floor(b[i][p[i]] / 0.9 + eps);
            li = ceil(li * 1.0 / a[i] - eps);
            ri = floor(ri * 1.0 / a[i] + eps);
            mxi = max(mxi, li);
            mni = min(mni, ri);
//            cout << i << ' ' << p[i] << ' ' << li << ' ' << ri << "!" << endl;
        }
//        cout << "mni, mxi = " << mni << ' ' << mxi << endl;
        if (mxi <= mni) {
            tot ++;
            for (int i = 1; i <= n; i ++) {
                p[i] ++;
                if (p[i] > m) {
                    return tot;
                }
            }
        } else {
            int id = -1;
            double mn = 1e10;
            for (int i = 1; i <= n; i ++) {
                double t = b[i][p[i]] * 1.0 / a[i];
                if (t < mn) mn = t, id = i;
            }
            p[id] ++;
            if (p[id] > m) {
                return tot;
            }
        }
    }
}

int main() {
    freopen("B-large (1).in", "r", stdin);
    freopen("B.out", "w", stdout);
    cin >> T;
    while (T --) {
        cin >> n >> m;
        for (int i = 1; i <= n; i ++)
            scanf("%d", &a[i]);
        for (int i = 1; i <= n; i ++) {
            for (int j = 1; j <= m; j ++)
                scanf("%d", &b[i][j]);
            sort(b[i] + 1, b[i] + 1 + m);
            p[i] = 1;
        }
        printf("Case #%d: %d\n", ++ cas, Calc());
    }
}
